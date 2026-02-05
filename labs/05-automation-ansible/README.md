# Lab 05: Automating OpenShift AI Workflows with Ansible

## Objective

In this lab, you will use **Ansible** to automate key components of the OpenShift AI
workflow built in previous labs.

By the end of this lab, you will be able to:

- Provision OpenShift namespaces and resources programmatically
- Deploy applications and workloads using declarative manifests
- Create repeatable, idempotent automation for OpenShift AI environments
- Lay the groundwork for CI/CD and enterprise-scale operations

This lab demonstrates how hands-on workflows from Labs 01–04 can be translated into
**reliable automation**.

---

## Environment assumptions

This lab has been validated with:

- OpenShift Container Platform 4.20
- OpenShift AI 3.x
- Ansible Core 2.14+
- `kubernetes.core` Ansible collection

Notes:
- This lab runs **outside** the OpenShift cluster
- You must have cluster-admin or appropriate RBAC permissions
- GPUs are optional and not required

---

## What you will automate

In this lab, Ansible will be used to:

- Create namespaces and base resources
- Apply Kubernetes and OpenShift manifests
- Prepare OpenShift AI projects for use
- Demonstrate a pattern for automating model workflows

This lab focuses on **structure and repeatability**, not exhaustive configuration.

---

## Step 1: Prepare your Ansible environment

Ensure you have Ansible installed locally:

```bash
ansible --version
```

Install required collections:

```bash
ansible-galaxy collection install kubernetes.core
```

Ensure your OpenShift login is active:

```bash
oc whoami
```

---

## Step 2: Create the Ansible project structure

From the repository root:

```
mkdir -p ansible/playbooks
mkdir -p ansible/roles/common
mkdir -p ansible/roles/label_studio
mkdir -p ansible/roles/openshift_ai
```

Recommended structure:

```
ansible/
├── playbooks/
│   └── deploy-openshift-ai.yml
├── roles/
│   ├── common/
│   ├── label_studio/
│   └── openshift_ai/
```

---

## Step 3: Create the main playbook

Create:

```
ansible/playbooks/deploy-openshift-ai.yml
```

```yaml
---
- name: Deploy OpenShift AI resources
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    label_studio_namespace: label-studio
    ai_project_namespace: computer-vision-lab

  roles:
    - common
    - label_studio
    - openshift_ai
```

---

## Step 4: Common role – namespace creation

Create:

```
ansible/roles/common/tasks/main.yml
```

```yaml
---
- name: Ensure Label Studio namespace exists
  kubernetes.core.k8s:
    api_version: v1
    kind: Namespace
    name: "{{ label_studio_namespace }}"
    state: present

- name: Ensure OpenShift AI namespace exists
  kubernetes.core.k8s:
    api_version: v1
    kind: Namespace
    name: "{{ ai_project_namespace }}"
    state: present
```

---

## Step 5: Label Studio role – deploy application

Create:

```
ansible/roles/label_studio/tasks/main.yml
```

```yaml
---
- name: Deploy Label Studio resources
  kubernetes.core.k8s:
    state: present
    namespace: "{{ label_studio_namespace }}"
    src: "{{ item }}"
  loop:
    - pvc.yaml
    - deployment.yaml
    - service.yaml
    - route.yaml
```

These YAML files should match the manifests used in Lab 01 and can be placed
under a shared manifests/label-studio/ directory.

---

## Step 6: OpenShift AI role – prepare project resources

Create:

```
ansible/roles/openshift_ai/tasks/main.yml
```

```yaml
---
- name: Apply OpenShift AI project resources
  kubernetes.core.k8s:
    state: present
    namespace: "{{ ai_project_namespace }}"
    src: "{{ item }}"
  loop:
    - dsproject.yaml
    - workbench.yaml
```

These manifests align with the manual steps completed in Lab 03.

---

## Step 7: Run the automation

From the repository root:

```
ansible-playbook ansible/playbooks/deploy-openshift-ai.yml
```

Ansible will:

- Create required namespaces

- Apply application manifests

- Skip unchanged resources on subsequent runs

This demonstrates idempotent automation.

---

## Step 8: Verify results

Confirm resources were created:

```bash
oc get projects
oc get pods -n label-studio
oc get pods -n computer-vision-lab
```

You should see:

- Label Studio deployed and running

- OpenShift AI project namespace created

- No errors on repeated playbook runs

---

## Completion criteria

You have successfully completed this lab when:

- Ansible runs without errors

- Namespaces are created automatically

- Application resources are deployed via playbooks

- Re-running the playbook makes no unnecessary changes

---

## Why this lab matters

This lab demonstrates:

- How manual workflows translate into automation

- How OpenShift AI environments can be standardized

- How teams reduce configuration drift

- How platform engineering practices apply to AI workloads

This is the foundation for CI/CD, GitOps, and large-scale AI operations.

---

## Next steps

In the final lab, you will explore enterprise hardening topics, including:

- Identity integration

- Centrify to SSSD migration patterns

- FIPS enablement considerations

Proceed to Lab 06: Identity and FIPS Hardening (Optional).
