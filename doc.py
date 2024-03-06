import subprocess
import argparse
import re
import logging

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Generate Kubernetes cluster state documentation with exclusion patterns.')
parser.add_argument('--exclude', action='append', help='Exclusion pattern for resources (can be used multiple times)', default=[])
args = parser.parse_args()

# Convert wildcard patterns to regex patterns
def wildcard_to_regex(pattern):
    pattern = re.escape(pattern)
    pattern = pattern.replace(r'\*', '.*')
    return re.compile(pattern + '$')

# Convert exclusion patterns to regex objects
exclusion_patterns = [wildcard_to_regex(pattern) for pattern in args.exclude]

# Function to check if a namespace/resource matches any exclusion pattern
def is_excluded(namespace, resource):
    resource_identifier = f"{namespace}/{resource}"
    for pattern in exclusion_patterns:
        if pattern.match(resource_identifier) or pattern.match(namespace + "/*") or pattern.match("*/" + resource):
            return True
    return False

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def create_markdown_table(headers, data):
    markdown = "| " + " | ".join(headers) + " |\n"
    markdown += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    for row in data:
        markdown += "| " + " | ".join(row) + " |\n"
    return markdown

def run_kubectl_command(command):
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        return output
    except subprocess.CalledProcessError as e:
        logging.info(f"No output returned from command: {command}")
        return None

def kubectl_data_and_headers(command, namespace=None):
    if namespace:
        command += f" -n {namespace}"
    return run_kubectl_command_parse(command)

def run_kubectl_command_parse(command):
    try:
        output = subprocess.check_output(command, shell=True, text=True).strip()
        if output:
            lines = output.split('\n')
            headers = lines[0].split()
            data = [line.split() for line in lines[1:]]
            return headers, data
        else:
            logging.info(f"No output returned from command: {command}")
            return [], []
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing command: {e}")
        return [], []

def get_container_images(resource_type, namespace=None):
    """
    Fetch container images from Deployments or DaemonSets.
    Args:
        resource_type (str): Either 'deployments' or 'daemonsets'.
        namespace (str): The namespace from which to fetch the resources. If None, fetches from all namespaces.
    Returns:
        list of tuples: Each tuple contains (namespace, name, container_images)
    """
    command = f"kubectl get {resource_type} {'-n ' + namespace if namespace else '--all-namespaces'} -o=jsonpath='{{range .items[*]}}{{.metadata.namespace}} {{.metadata.name}} {{range .spec.template.spec.containers[*]}} {{.image}}{{end}}{{\"\\n\"}}{{end}}'"
    output = run_kubectl_command(command)
    if not output:
        return []
    
    data = []
    lines = output.strip().split('\n')
    for line in lines:
        parts = line.rsplit(' ')
        ns, name = parts[0], parts[1]
        images = parts[2:]
        images = [element for element in images if element not in [None, '']]

        data.append((ns, name, ", ".join(images)))
    return data


def get_pod_names_from_endpoints(namespace, endpoints):
    pod_names = []
    if "<none>" in endpoints or endpoints == "None" or endpoints == "Error fetching":
        return "None"
    endpoint_list = endpoints.split(',')
    for endpoint in endpoint_list:
        ip = endpoint.split(':')[0].strip()
        command = f"kubectl get pods --all-namespaces -o wide | grep {ip}"
        output = run_kubectl_command(command)
        if output:
            lines = output.strip().split('\n')
            pod_name = lines[0].split()[1] if lines else "Pod not found"
            pod_names.append(pod_name)
        else:
            pod_names.append("Error fetching pod")
    return ", ".join(pod_names)

def get_services_and_endpoints_with_pods(namespace=None):
    command = "kubectl get svc"
    if namespace:
        command += f" -n {namespace}"
    else:
        command += " --all-namespaces"
    output = run_kubectl_command(command)
    if not output:
        return [], []
    
    lines = output.strip().split('\n')
    data = []
    for line in lines[1:]:  # Skip the header row
        parts = line.split()
        ns = parts[0] if not namespace else namespace
        name = parts[1]
        describe_command = f"kubectl describe svc {name} -n {ns}"
        describe_output = run_kubectl_command(describe_command)
        if describe_output:
            endpoints_line = [line for line in describe_output.split('\n') if "Endpoints:" in line]
            endpoints = endpoints_line[0].split(":", 1)[1].strip() if endpoints_line else "None"
            pod_names = get_pod_names_from_endpoints(ns, endpoints)
        else:
            endpoints = "Error fetching"
            pod_names = "Error fetching pod"
        data.append([ns, name, endpoints, pod_names])

        headers = headers = ["NAMESPACE", "NAME" "TYPE", "ENDPOINTS", "POD NAMES"]

    return headers, data

def get_namespaces():
    command = "kubectl get namespaces -o=jsonpath='{.items[*].metadata.name}'"
    output = run_kubectl_command(command)
    if output:
        namespaces = output.strip().split()
        return namespaces
    return []

def generate_markdown_for_namespace(md_file, namespace=None):
    resources = ["deployments", "ds", "sts", "ingress", "svc", "pvc", "sa"]
    for resource in resources:
        if is_excluded(namespace if namespace else "*", resource):
            continue  # Skip this resource due to an exclusion match

        md_file.write(f"## {resource.upper()}\n\n")
        command = f"kubectl get {resource} --all-namespaces" if not namespace else f"kubectl get {resource}"
        headers, data = kubectl_data_and_headers(command, namespace)
        if headers and data:
            md_file.write(create_markdown_table(headers, data))
            # subchapter for containers images when applying
            if resource in ["deployments", "ds", "sts"]:
                resource_type = 'deployments' if resource == 'deployments' else 'daemonsets'
                images_data = get_container_images(resource_type, namespace)
                if images_data:
                    headers = ["NAMESPACE", "NAME", "CONTAINER IMAGES"]
                    md_file.write(f"### {resource.upper()} Container Images\n\n")
                    md_file.write(create_markdown_table(headers, images_data))
                else:
                    md_file.write(f"No container images found for {resource}.\n\n")

        else:
            md_file.write(f"No {resource} found.\n\n")

    if is_excluded(namespace if namespace else "*", "svc-ep-pods"):
        return

    # Services and endpoints with pods
    md_file.write("## Services and their endpoints (including pod names)\n\n")
    headers, data = get_services_and_endpoints_with_pods(namespace)
    if headers and data:
        md_file.write(create_markdown_table(headers, data))
    else:
        md_file.write("No services or endpoints found.\n\n")

def generate_markdown():
    filename = "cluster_state.md"
    logging.info(f"Starting to generate markdown documentation in {filename}")
    
    # Start with collecting namespaces to build TOC
    namespaces = get_namespaces()
    toc_items = [f"- [Namespace: {namespace}](#namespace-{namespace.lower().replace(' ', '-')})" for namespace in namespaces]
    toc_items.append("- [Final Chapter: All Resources (No Namespace Filter)](#final-chapter-all-resources-no-namespace-filter)")

    with open(filename, 'w') as md_file:
        md_file.write("# Cluster State Documentation\n\n")
        
        # Write TOC
        md_file.write("## Table of Contents\n\n")
        md_file.writelines("\n".join(toc_items))
        md_file.write("\n\n")

        if not namespaces:
            # If no namespaces are found or if we want to generate for all namespaces regardless
            generate_markdown_for_namespace(md_file)
        else:
            for namespace in namespaces:
                # Adjust the header to include a linkable ID
                md_file.write(f'<a name="namespace-{namespace.lower().replace(" ", "-")}"></a>\n')
                md_file.write(f"# Namespace: {namespace}\n\n")
                generate_markdown_for_namespace(md_file, namespace)
            # Additional section for all resources without namespace filter
            md_file.write('<a name="final-chapter-all-resources-no-namespace-filter"></a>\n')
            md_file.write("# Final Chapter: All Resources (No Namespace Filter)\n\n")
            generate_markdown_for_namespace(md_file, None)

        md_file.write("""
# aditional chapter just for testing
```mermaid
flowchart TD
A[Christmas] -->|Get money| B(Go shopping)
B --> C{Let me think}
C -->|One| D[Laptop]
C -->|Two| E[iPhone]
C -->|Three| F[fa:fa-car Car]
```
    """)
    logging.info(f"Markdown documentation generated in {filename}")

generate_markdown()
