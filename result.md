# Cluster State Documentation

## Table of Contents

- [Namespace: kube-system](#namespace-kube-system)
- [Namespace: kube-public](#namespace-kube-public)
- [Namespace: kube-node-lease](#namespace-kube-node-lease)
- [Namespace: default](#namespace-default)
- [Namespace: tigera-operator](#namespace-tigera-operator)
- [Namespace: calico-system](#namespace-calico-system)
- [Namespace: calico-apiserver](#namespace-calico-apiserver)
- [Namespace: cdi](#namespace-cdi)
- [Namespace: kubevirt](#namespace-kubevirt)
- [Namespace: cluster-network-addons](#namespace-cluster-network-addons)
- [Final Chapter: All Resources (No Namespace Filter)](#final-chapter-all-resources-no-namespace-filter)

<a name="namespace-kube-system"></a>
# Namespace: kube-system

<a name="namespace-kube-public"></a>
# Namespace: kube-public

## DEPLOYMENTS

No deployments found.

## DS

No ds found.

## STS

No sts found.

## INGRESS

No ingress found.

## SVC

No svc found.

## PVC

No pvc found.

## SA

| NAME | SECRETS | AGE |
| --- | --- | --- |
| default | 0 | 20d |
## Services and their endpoints (including pod names)

No services or endpoints found.

<a name="namespace-kube-node-lease"></a>
# Namespace: kube-node-lease

## DEPLOYMENTS

No deployments found.

## DS

No ds found.

## STS

No sts found.

## INGRESS

No ingress found.

## SVC

No svc found.

## PVC

No pvc found.

## SA

| NAME | SECRETS | AGE |
| --- | --- | --- |
| default | 0 | 20d |
## Services and their endpoints (including pod names)

No services or endpoints found.

<a name="namespace-default"></a>
# Namespace: default

## DEPLOYMENTS

No deployments found.

## DS

No ds found.

## STS

No sts found.

## INGRESS

No ingress found.

## SVC

| NAME | TYPE | CLUSTER-IP | EXTERNAL-IP | PORT(S) | AGE |
| --- | --- | --- | --- | --- | --- |
| kubernetes | ClusterIP | 10.43.0.1 | <none> | 443/TCP | 20d |
## PVC

No pvc found.

## SA

| NAME | SECRETS | AGE |
| --- | --- | --- |
| default | 0 | 20d |
## Services and their endpoints (including pod names)

| NAMESPACE | NAMETYPE | ENDPOINTS | POD NAMES |
| --- | --- | --- | --- |
| default | ClusterIP | Error fetching | Error fetching pod |
<a name="namespace-tigera-operator"></a>
# Namespace: tigera-operator

## DEPLOYMENTS

| NAME | READY | UP-TO-DATE | AVAILABLE | AGE |
| --- | --- | --- | --- | --- |
| tigera-operator | 1/1 | 1 | 1 | 20d |
### DEPLOYMENTS Container Images

| NAMESPACE | NAME | CONTAINER IMAGES |
| --- | --- | --- |
| tigera-operator | tigera-operator | quay.io/tigera/operator:v1.32.3 |
## DS

No ds found.

## STS

No sts found.

## INGRESS

No ingress found.

## SVC

No svc found.

## PVC

No pvc found.

## SA

| NAME | SECRETS | AGE |
| --- | --- | --- |
| default | 0 | 20d |
| tigera-operator | 0 | 20d |
## Services and their endpoints (including pod names)

No services or endpoints found.

<a name="namespace-calico-system"></a>
# Namespace: calico-system

## DEPLOYMENTS

| NAME | READY | UP-TO-DATE | AVAILABLE | AGE |
| --- | --- | --- | --- | --- |
| calico-kube-controllers | 0/1 | 1 | 0 | 20d |
| calico-typha | 1/1 | 1 | 1 | 20d |
### DEPLOYMENTS Container Images

| NAMESPACE | NAME | CONTAINER IMAGES |
| --- | --- | --- |
| calico-system | calico-kube-controllers | docker.io/calico/kube-controllers:v3.27.0 |
| calico-system | calico-typha | docker.io/calico/typha:v3.27.0 |
## DS

| NAME | DESIRED | CURRENT | READY | UP-TO-DATE | AVAILABLE | NODE | SELECTOR | AGE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| csi-node-driver | 1 | 1 | 0 | 1 | 0 | kubernetes.io/os=linux | 20d |
| calico-node | 1 | 1 | 1 | 1 | 1 | kubernetes.io/os=linux | 20d |
### DS Container Images

| NAMESPACE | NAME | CONTAINER IMAGES |
| --- | --- | --- |
| calico-system | csi-node-driver | docker.io/calico/csi:v3.27.0, docker.io/calico/node-driver-registrar:v3.27.0 |
| calico-system | calico-node | docker.io/calico/node:v3.27.0 |
## STS

No sts found.

## INGRESS

No ingress found.

## SVC

| NAME | TYPE | CLUSTER-IP | EXTERNAL-IP | PORT(S) | AGE |
| --- | --- | --- | --- | --- | --- |
| calico-typha | ClusterIP | 10.43.156.99 | <none> | 5473/TCP | 20d |
| calico-kube-controllers-metrics | ClusterIP | None | <none> | 9094/TCP | 20d |
## PVC

No pvc found.

## SA

| NAME | SECRETS | AGE |
| --- | --- | --- |
| default | 0 | 20d |
| calico-typha | 0 | 20d |
| calico-node | 0 | 20d |
| calico-cni-plugin | 0 | 20d |
| calico-kube-controllers | 0 | 20d |
## Services and their endpoints (including pod names)

| NAMESPACE | NAMETYPE | ENDPOINTS | POD NAMES |
| --- | --- | --- | --- |
| calico-system | ClusterIP | Error fetching | Error fetching pod |
| calico-system | ClusterIP | Error fetching | Error fetching pod |
<a name="namespace-calico-apiserver"></a>
# Namespace: calico-apiserver

## DEPLOYMENTS

| NAME | READY | UP-TO-DATE | AVAILABLE | AGE |
| --- | --- | --- | --- | --- |
| calico-apiserver | 0/2 | 2 | 0 | 20d |
### DEPLOYMENTS Container Images

| NAMESPACE | NAME | CONTAINER IMAGES |
| --- | --- | --- |
| calico-apiserver | calico-apiserver | docker.io/calico/apiserver:v3.27.0 |
## DS

No ds found.

## STS

No sts found.

## INGRESS

No ingress found.

## SVC

| NAME | TYPE | CLUSTER-IP | EXTERNAL-IP | PORT(S) | AGE |
| --- | --- | --- | --- | --- | --- |
| calico-api | ClusterIP | 10.43.39.252 | <none> | 443/TCP | 20d |
## PVC

No pvc found.

## SA

| NAME | SECRETS | AGE |
| --- | --- | --- |
| default | 0 | 20d |
| calico-apiserver | 0 | 20d |
## Services and their endpoints (including pod names)

| NAMESPACE | NAMETYPE | ENDPOINTS | POD NAMES |
| --- | --- | --- | --- |
| calico-apiserver | ClusterIP | Error fetching | Error fetching pod |
<a name="namespace-cdi"></a>
# Namespace: cdi

## DEPLOYMENTS

| NAME | READY | UP-TO-DATE | AVAILABLE | AGE |
| --- | --- | --- | --- | --- |
| cdi-apiserver | 0/1 | 1 | 0 | 20d |
| cdi-deployment | 0/1 | 1 | 0 | 20d |
| cdi-operator | 0/1 | 1 | 0 | 20d |
| cdi-uploadproxy | 0/1 | 1 | 0 | 20d |
### DEPLOYMENTS Container Images

| NAMESPACE | NAME | CONTAINER IMAGES |
| --- | --- | --- |
| cdi | cdi-apiserver | quay.io/kubevirt/cdi-apiserver:v1.58.1 |
| cdi | cdi-deployment | quay.io/kubevirt/cdi-controller:v1.58.1 |
| cdi | cdi-operator | quay.io/kubevirt/cdi-operator:v1.58.1 |
| cdi | cdi-uploadproxy | quay.io/kubevirt/cdi-uploadproxy:v1.58.1 |
## DS

No ds found.

## STS

No sts found.

## INGRESS

No ingress found.

## SVC

| NAME | TYPE | CLUSTER-IP | EXTERNAL-IP | PORT(S) | AGE |
| --- | --- | --- | --- | --- | --- |
| cdi-api | ClusterIP | 10.43.125.239 | <none> | 443/TCP | 20d |
| cdi-prometheus-metrics | ClusterIP | 10.43.223.94 | <none> | 8080/TCP | 20d |
| cdi-uploadproxy | ClusterIP | 10.43.63.130 | <none> | 443/TCP | 20d |
## PVC

No pvc found.

## SA

| NAME | SECRETS | AGE |
| --- | --- | --- |
| default | 0 | 20d |
| cdi-operator | 0 | 20d |
| cdi-apiserver | 0 | 20d |
| cdi-sa | 0 | 20d |
| cdi-uploadproxy | 0 | 20d |
| cdi-cronjob | 0 | 20d |
## Services and their endpoints (including pod names)

| NAMESPACE | NAMETYPE | ENDPOINTS | POD NAMES |
| --- | --- | --- | --- |
| cdi | ClusterIP | Error fetching | Error fetching pod |
| cdi | ClusterIP | Error fetching | Error fetching pod |
| cdi | ClusterIP | Error fetching | Error fetching pod |
<a name="namespace-kubevirt"></a>
# Namespace: kubevirt

## DEPLOYMENTS

| NAME | READY | UP-TO-DATE | AVAILABLE | AGE |
| --- | --- | --- | --- | --- |
| virt-api | 0/1 | 1 | 0 | 20d |
| virt-controller | 0/2 | 2 | 0 | 20d |
| virt-operator | 0/2 | 2 | 0 | 20d |
### DEPLOYMENTS Container Images

| NAMESPACE | NAME | CONTAINER IMAGES |
| --- | --- | --- |
| kubevirt | virt-api | quay.io/kubevirt/virt-api:v1.1.1 |
| kubevirt | virt-controller | quay.io/kubevirt/virt-controller:v1.1.1 |
| kubevirt | virt-operator | quay.io/kubevirt/virt-operator:v1.1.1 |
## DS

| NAME | DESIRED | CURRENT | READY | UP-TO-DATE | AVAILABLE | NODE | SELECTOR | AGE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| virt-handler | 1 | 1 | 0 | 1 | 0 | kubernetes.io/os=linux | 20d |
### DS Container Images

| NAMESPACE | NAME | CONTAINER IMAGES |
| --- | --- | --- |
| kubevirt | virt-handler | quay.io/kubevirt/virt-handler:v1.1.1 |
## STS

No sts found.

## INGRESS

No ingress found.

## SVC

| NAME | TYPE | CLUSTER-IP | EXTERNAL-IP | PORT(S) | AGE |
| --- | --- | --- | --- | --- | --- |
| kubevirt-prometheus-metrics | ClusterIP | None | <none> | 443/TCP | 20d |
| virt-api | ClusterIP | 10.43.22.145 | <none> | 443/TCP | 20d |
| kubevirt-operator-webhook | ClusterIP | 10.43.126.96 | <none> | 443/TCP | 20d |
| virt-exportproxy | ClusterIP | 10.43.189.95 | <none> | 443/TCP | 20d |
## PVC

No pvc found.

## SA

| NAME | SECRETS | AGE |
| --- | --- | --- |
| default | 0 | 20d |
| kubevirt-operator | 0 | 20d |
| kubevirt-apiserver | 0 | 20d |
| kubevirt-controller | 0 | 20d |
| kubevirt-handler | 0 | 20d |
| kubevirt-exportproxy | 0 | 20d |
## Services and their endpoints (including pod names)

| NAMESPACE | NAMETYPE | ENDPOINTS | POD NAMES |
| --- | --- | --- | --- |
| kubevirt | ClusterIP | Error fetching | Error fetching pod |
| kubevirt | ClusterIP | Error fetching | Error fetching pod |
| kubevirt | ClusterIP | Error fetching | Error fetching pod |
| kubevirt | ClusterIP | Error fetching | Error fetching pod |
<a name="namespace-cluster-network-addons"></a>
# Namespace: cluster-network-addons

## DEPLOYMENTS

| NAME | READY | UP-TO-DATE | AVAILABLE | AGE |
| --- | --- | --- | --- | --- |
| cluster-network-addons-operator | 0/1 | 1 | 0 | 20d |
| kubemacpool-mac-controller-manager | 0/1 | 1 | 0 | 20d |
| secondary-dns | 0/1 | 1 | 0 | 20d |
| kubemacpool-cert-manager | 0/1 | 1 | 0 | 20d |
### DEPLOYMENTS Container Images

| NAMESPACE | NAME | CONTAINER IMAGES |
| --- | --- | --- |
| cluster-network-addons | cluster-network-addons-operator | quay.io/kubevirt/cluster-network-addons-operator:v0.90.1, quay.io/openshift/origin-kube-rbac-proxy@sha256:baedb268ac66456018fb30af395bb3d69af5fff3252ff5d549f0231b1ebb6901 |
| cluster-network-addons | kubemacpool-mac-controller-manager | quay.io/kubevirt/kubemacpool@sha256:2f7a4ed0532909176b21eb3b80dec88a14e4f23d0c0aae129acd699636d058a3, quay.io/openshift/origin-kube-rbac-proxy@sha256:baedb268ac66456018fb30af395bb3d69af5fff3252ff5d549f0231b1ebb6901 |
| cluster-network-addons | secondary-dns | registry.k8s.io/coredns/coredns@sha256:a0ead06651cf580044aeb0a0feba63591858fb2e43ade8c9dea45a6a89ae7e5e, ghcr.io/kubevirt/kubesecondarydns@sha256:e87e829380a1e576384145f78ccaa885ba1d5690d5de7d0b73d40cfb804ea24d |
| cluster-network-addons | kubemacpool-cert-manager | quay.io/kubevirt/kubemacpool@sha256:2f7a4ed0532909176b21eb3b80dec88a14e4f23d0c0aae129acd699636d058a3 |
## DS

| NAME | DESIRED | CURRENT | READY | UP-TO-DATE | AVAILABLE | NODE | SELECTOR | AGE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bridge-marker | 1 | 1 | 1 | 1 | 1 | kubernetes.io/os=linux | 20d |
| kube-cni-linux-bridge-plugin | 1 | 1 | 0 | 1 | 0 | kubernetes.io/os=linux | 20d |
| macvtap-cni | 1 | 1 | 0 | 1 | 0 | kubernetes.io/os=linux | 20d |
| multus | 1 | 1 | 0 | 1 | 0 | kubernetes.io/os=linux | 20d |
### DS Container Images

| NAMESPACE | NAME | CONTAINER IMAGES |
| --- | --- | --- |
| cluster-network-addons | bridge-marker | quay.io/kubevirt/bridge-marker@sha256:bba066e3b5ff3fb8c5e20861fe8abe51e3c9b50ad6ce3b2616af9cb5479a06d0 |
| cluster-network-addons | kube-cni-linux-bridge-plugin | quay.io/kubevirt/cni-default-plugins@sha256:825e3f9fec1996c54a52cec806154945b38f76476b160d554c36e38dfffe5e61 |
| cluster-network-addons | macvtap-cni | quay.io/kubevirt/macvtap-cni@sha256:850b89343ace7c7ea6b18dd8e11964613974e9d1f7377af03854d407fb15230a |
| cluster-network-addons | multus | ghcr.io/k8snetworkplumbingwg/multus-cni@sha256:3fbcc32bd4e4d15bd93c96def784a229cd84cca27942bf4858b581f31c97ee02 |
## STS

No sts found.

## INGRESS

No ingress found.

## SVC

| NAME | TYPE | CLUSTER-IP | EXTERNAL-IP | PORT(S) | AGE |
| --- | --- | --- | --- | --- | --- |
| kubemacpool-service | ClusterIP | 10.43.228.248 | <none> | 443/TCP | 20d |
## PVC

No pvc found.

## SA

| NAME | SECRETS | AGE |
| --- | --- | --- |
| default | 0 | 20d |
| cluster-network-addons-operator | 0 | 20d |
| multus | 0 | 20d |
| bridge-marker | 0 | 20d |
| secondary | 0 | 20d |
## Services and their endpoints (including pod names)

| NAMESPACE | NAMETYPE | ENDPOINTS | POD NAMES |
| --- | --- | --- | --- |
| cluster-network-addons | ClusterIP | Error fetching | Error fetching pod |
<a name="final-chapter-all-resources-no-namespace-filter"></a>
# Final Chapter: All Resources (No Namespace Filter)

## DEPLOYMENTS

| NAMESPACE | NAME | READY | UP-TO-DATE | AVAILABLE | AGE |
| --- | --- | --- | --- | --- | --- |
| cdi | cdi-apiserver | 0/1 | 1 | 0 | 20d |
| calico-apiserver | calico-apiserver | 0/2 | 2 | 0 | 20d |
| calico-system | calico-kube-controllers | 0/1 | 1 | 0 | 20d |
| cdi | cdi-deployment | 0/1 | 1 | 0 | 20d |
| cdi | cdi-operator | 0/1 | 1 | 0 | 20d |
| cdi | cdi-uploadproxy | 0/1 | 1 | 0 | 20d |
| cluster-network-addons | cluster-network-addons-operator | 0/1 | 1 | 0 | 20d |
| cluster-network-addons | kubemacpool-mac-controller-manager | 0/1 | 1 | 0 | 20d |
| cluster-network-addons | secondary-dns | 0/1 | 1 | 0 | 20d |
| cluster-network-addons | kubemacpool-cert-manager | 0/1 | 1 | 0 | 20d |
| kube-system | coredns | 0/1 | 1 | 0 | 20d |
| kube-system | local-path-provisioner | 0/1 | 1 | 0 | 20d |
| kube-system | metrics-server | 0/1 | 1 | 0 | 20d |
| kubevirt | virt-api | 0/1 | 1 | 0 | 20d |
| kubevirt | virt-controller | 0/2 | 2 | 0 | 20d |
| kubevirt | virt-operator | 0/2 | 2 | 0 | 20d |
| tigera-operator | tigera-operator | 1/1 | 1 | 1 | 20d |
| calico-system | calico-typha | 1/1 | 1 | 1 | 20d |
### DEPLOYMENTS Container Images

| NAMESPACE | NAME | CONTAINER IMAGES |
| --- | --- | --- |
| cdi | cdi-apiserver | quay.io/kubevirt/cdi-apiserver:v1.58.1 |
| calico-apiserver | calico-apiserver | docker.io/calico/apiserver:v3.27.0 |
| calico-system | calico-kube-controllers | docker.io/calico/kube-controllers:v3.27.0 |
| cdi | cdi-deployment | quay.io/kubevirt/cdi-controller:v1.58.1 |
| cdi | cdi-operator | quay.io/kubevirt/cdi-operator:v1.58.1 |
| cdi | cdi-uploadproxy | quay.io/kubevirt/cdi-uploadproxy:v1.58.1 |
| cluster-network-addons | cluster-network-addons-operator | quay.io/kubevirt/cluster-network-addons-operator:v0.90.1, quay.io/openshift/origin-kube-rbac-proxy@sha256:baedb268ac66456018fb30af395bb3d69af5fff3252ff5d549f0231b1ebb6901 |
| cluster-network-addons | kubemacpool-mac-controller-manager | quay.io/kubevirt/kubemacpool@sha256:2f7a4ed0532909176b21eb3b80dec88a14e4f23d0c0aae129acd699636d058a3, quay.io/openshift/origin-kube-rbac-proxy@sha256:baedb268ac66456018fb30af395bb3d69af5fff3252ff5d549f0231b1ebb6901 |
| cluster-network-addons | secondary-dns | registry.k8s.io/coredns/coredns@sha256:a0ead06651cf580044aeb0a0feba63591858fb2e43ade8c9dea45a6a89ae7e5e, ghcr.io/kubevirt/kubesecondarydns@sha256:e87e829380a1e576384145f78ccaa885ba1d5690d5de7d0b73d40cfb804ea24d |
| cluster-network-addons | kubemacpool-cert-manager | quay.io/kubevirt/kubemacpool@sha256:2f7a4ed0532909176b21eb3b80dec88a14e4f23d0c0aae129acd699636d058a3 |
| kube-system | coredns | rancher/mirrored-coredns-coredns:1.10.1 |
| kube-system | local-path-provisioner | rancher/local-path-provisioner:v0.0.24 |
| kube-system | metrics-server | rancher/mirrored-metrics-server:v0.6.3 |
| kubevirt | virt-api | quay.io/kubevirt/virt-api:v1.1.1 |
| kubevirt | virt-controller | quay.io/kubevirt/virt-controller:v1.1.1 |
| kubevirt | virt-operator | quay.io/kubevirt/virt-operator:v1.1.1 |
| tigera-operator | tigera-operator | quay.io/tigera/operator:v1.32.3 |
| calico-system | calico-typha | docker.io/calico/typha:v3.27.0 |
## DS

| NAMESPACE | NAME | DESIRED | CURRENT | READY | UP-TO-DATE | AVAILABLE | NODE | SELECTOR | AGE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cluster-network-addons | bridge-marker | 1 | 1 | 1 | 1 | 1 | kubernetes.io/os=linux | 20d |
| calico-system | csi-node-driver | 1 | 1 | 0 | 1 | 0 | kubernetes.io/os=linux | 20d |
| cluster-network-addons | kube-cni-linux-bridge-plugin | 1 | 1 | 0 | 1 | 0 | kubernetes.io/os=linux | 20d |
| cluster-network-addons | macvtap-cni | 1 | 1 | 0 | 1 | 0 | kubernetes.io/os=linux | 20d |
| cluster-network-addons | multus | 1 | 1 | 0 | 1 | 0 | kubernetes.io/os=linux | 20d |
| kubevirt | virt-handler | 1 | 1 | 0 | 1 | 0 | kubernetes.io/os=linux | 20d |
| calico-system | calico-node | 1 | 1 | 1 | 1 | 1 | kubernetes.io/os=linux | 20d |
### DS Container Images

| NAMESPACE | NAME | CONTAINER IMAGES |
| --- | --- | --- |
| cluster-network-addons | bridge-marker | quay.io/kubevirt/bridge-marker@sha256:bba066e3b5ff3fb8c5e20861fe8abe51e3c9b50ad6ce3b2616af9cb5479a06d0 |
| calico-system | csi-node-driver | docker.io/calico/csi:v3.27.0, docker.io/calico/node-driver-registrar:v3.27.0 |
| cluster-network-addons | kube-cni-linux-bridge-plugin | quay.io/kubevirt/cni-default-plugins@sha256:825e3f9fec1996c54a52cec806154945b38f76476b160d554c36e38dfffe5e61 |
| cluster-network-addons | macvtap-cni | quay.io/kubevirt/macvtap-cni@sha256:850b89343ace7c7ea6b18dd8e11964613974e9d1f7377af03854d407fb15230a |
| cluster-network-addons | multus | ghcr.io/k8snetworkplumbingwg/multus-cni@sha256:3fbcc32bd4e4d15bd93c96def784a229cd84cca27942bf4858b581f31c97ee02 |
| kubevirt | virt-handler | quay.io/kubevirt/virt-handler:v1.1.1 |
| calico-system | calico-node | docker.io/calico/node:v3.27.0 |
## STS

No sts found.

## INGRESS

No ingress found.

## SVC

| NAMESPACE | NAME | TYPE | CLUSTER-IP | EXTERNAL-IP | PORT(S) | AGE |
| --- | --- | --- | --- | --- | --- | --- |
| default | kubernetes | ClusterIP | 10.43.0.1 | <none> | 443/TCP | 20d |
| kube-system | kube-dns | ClusterIP | 10.43.0.10 | <none> | 53/UDP,53/TCP,9153/TCP | 20d |
| kube-system | metrics-server | ClusterIP | 10.43.63.165 | <none> | 443/TCP | 20d |
| calico-system | calico-typha | ClusterIP | 10.43.156.99 | <none> | 5473/TCP | 20d |
| calico-system | calico-kube-controllers-metrics | ClusterIP | None | <none> | 9094/TCP | 20d |
| calico-apiserver | calico-api | ClusterIP | 10.43.39.252 | <none> | 443/TCP | 20d |
| cdi | cdi-api | ClusterIP | 10.43.125.239 | <none> | 443/TCP | 20d |
| cdi | cdi-prometheus-metrics | ClusterIP | 10.43.223.94 | <none> | 8080/TCP | 20d |
| cdi | cdi-uploadproxy | ClusterIP | 10.43.63.130 | <none> | 443/TCP | 20d |
| cluster-network-addons | kubemacpool-service | ClusterIP | 10.43.228.248 | <none> | 443/TCP | 20d |
| kubevirt | kubevirt-prometheus-metrics | ClusterIP | None | <none> | 443/TCP | 20d |
| kubevirt | virt-api | ClusterIP | 10.43.22.145 | <none> | 443/TCP | 20d |
| kubevirt | kubevirt-operator-webhook | ClusterIP | 10.43.126.96 | <none> | 443/TCP | 20d |
| kubevirt | virt-exportproxy | ClusterIP | 10.43.189.95 | <none> | 443/TCP | 20d |
## PVC

No pvc found.

## SA

| NAMESPACE | NAME | SECRETS | AGE |
| --- | --- | --- | --- |
| kube-system | ephemeral-volume-controller | 0 | 20d |
| kube-system | expand-controller | 0 | 20d |
| kube-system | resourcequota-controller | 0 | 20d |
| kube-system | horizontal-pod-autoscaler | 0 | 20d |
| kube-system | disruption-controller | 0 | 20d |
| kube-system | node-controller | 0 | 20d |
| kube-system | persistent-volume-binder | 0 | 20d |
| kube-system | root-ca-cert-publisher | 0 | 20d |
| kube-system | endpoint-controller | 0 | 20d |
| kube-system | namespace-controller | 0 | 20d |
| kube-system | ttl-controller | 0 | 20d |
| kube-system | endpointslicemirroring-controller | 0 | 20d |
| kube-system | job-controller | 0 | 20d |
| kube-system | deployment-controller | 0 | 20d |
| kube-system | replicaset-controller | 0 | 20d |
| kube-system | token-cleaner | 0 | 20d |
| kube-system | clusterrole-aggregation-controller | 0 | 20d |
| kube-system | service-account-controller | 0 | 20d |
| kube-system | pv-protection-controller | 0 | 20d |
| kube-system | statefulset-controller | 0 | 20d |
| kube-system | cronjob-controller | 0 | 20d |
| kube-system | certificate-controller | 0 | 20d |
| kube-system | coredns | 0 | 20d |
| kube-system | local-path-provisioner-service-account | 0 | 20d |
| kube-system | svclb | 0 | 20d |
| kube-system | metrics-server | 0 | 20d |
| kube-system | pvc-protection-controller | 0 | 20d |
| kube-system | pod-garbage-collector | 0 | 20d |
| kube-system | attachdetach-controller | 0 | 20d |
| kube-system | ttl-after-finished-controller | 0 | 20d |
| kube-system | generic-garbage-collector | 0 | 20d |
| kube-system | daemon-set-controller | 0 | 20d |
| kube-system | endpointslice-controller | 0 | 20d |
| kube-system | replication-controller | 0 | 20d |
| default | default | 0 | 20d |
| kube-node-lease | default | 0 | 20d |
| kube-public | default | 0 | 20d |
| kube-system | default | 0 | 20d |
| tigera-operator | default | 0 | 20d |
| tigera-operator | tigera-operator | 0 | 20d |
| calico-system | default | 0 | 20d |
| calico-system | calico-typha | 0 | 20d |
| calico-system | calico-node | 0 | 20d |
| calico-system | calico-cni-plugin | 0 | 20d |
| calico-system | calico-kube-controllers | 0 | 20d |
| calico-apiserver | default | 0 | 20d |
| calico-apiserver | calico-apiserver | 0 | 20d |
| kubevirt | default | 0 | 20d |
| kubevirt | kubevirt-operator | 0 | 20d |
| cdi | default | 0 | 20d |
| cdi | cdi-operator | 0 | 20d |
| cdi | cdi-apiserver | 0 | 20d |
| cdi | cdi-sa | 0 | 20d |
| cdi | cdi-uploadproxy | 0 | 20d |
| cdi | cdi-cronjob | 0 | 20d |
| cluster-network-addons | default | 0 | 20d |
| cluster-network-addons | cluster-network-addons-operator | 0 | 20d |
| cluster-network-addons | multus | 0 | 20d |
| cluster-network-addons | bridge-marker | 0 | 20d |
| cluster-network-addons | secondary | 0 | 20d |
| kubevirt | kubevirt-apiserver | 0 | 20d |
| kubevirt | kubevirt-controller | 0 | 20d |
| kubevirt | kubevirt-handler | 0 | 20d |
| kubevirt | kubevirt-exportproxy | 0 | 20d |
## Services and their endpoints (including pod names)

| NAMESPACE | NAMETYPE | ENDPOINTS | POD NAMES |
| --- | --- | --- | --- |
| default | kubernetes | 172.19.34.189:6443 | bridge-marker-2vkkt |
| kube-system | kube-dns | <none> | None |
| kube-system | metrics-server | <none> | None |
| calico-system | calico-typha | 172.19.34.189:5473 | bridge-marker-2vkkt |
| calico-system | calico-kube-controllers-metrics | <none> | None |
| calico-apiserver | calico-api | <none> | None |
| cdi | cdi-api | <none> | None |
| cdi | cdi-prometheus-metrics | <none> | None |
| cdi | cdi-uploadproxy | <none> | None |
| cluster-network-addons | kubemacpool-service | <none> | None |
| kubevirt | kubevirt-prometheus-metrics | <none> | None |
| kubevirt | virt-api | <none> | None |
| kubevirt | kubevirt-operator-webhook | <none> | None |
| kubevirt | virt-exportproxy | <none> | None |

# aditional chapter just for testing
```mermaid
flowchart TD
A[Christmas] -->|Get money| B(Go shopping)
B --> C{Let me think}
C -->|One| D[Laptop]
C -->|Two| E[iPhone]
C -->|Three| F[fa:fa-car Car]
```
    