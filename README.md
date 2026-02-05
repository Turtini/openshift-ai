# OpenShift AI

Hands-on labs, reference architectures, and automation examples for building, training, and operating workloads with **Red Hat OpenShift AI**.

This repository contains practical, reproducible content designed for platform engineers, architects, and practitioners who want to understand how OpenShift AI is used in real environments — from data preparation and model training to automation and operational hardening.

---

## What this repository is

This repository provides:

- **Hands-on labs** you can follow end to end
- **Console-first workflows** with optional automation paths
- **Reference manifests and Ansible examples**
- **Clear validation steps** so you know what “good” looks like

The focus is on **how things actually work** on OpenShift, not on abstract examples or marketing demos.

---

## What this repository is not

- This is **not** a fork of any Red Hat product
- This is **not** an SDK or API mirror
- This is **not** intended to replace official documentation

Instead, it complements upstream documentation with concrete, runnable examples.

---

## Lab environment assumptions

The labs in this repository are designed to work in common development and enablement environments, including:

- OpenShift Container Platform 4.20
- OpenShift AI 3.x
- CodeReady Containers (CRC) 2.48

Where relevant:
- **GPUs are optional**
- **Git integration is optional**
- CPU-only paths are always documented

Each lab explicitly calls out prerequisites and environment expectations.

---

### Directory overview

- **labs/**  
  Step-by-step exercises with clear objectives and completion criteria.

- **manifests/**  
  Kubernetes and OpenShift YAML used by the labs.

- **ansible/**  
  Automation examples for repeatable deployments and configuration.

- **validation/**  
  Commands and checks used to confirm successful lab completion.

---

## Current labs

### Lab 01: Deploy Label Studio on OpenShift
Deploy Label Studio using a standard Deployment, Service, Route, and PVC pattern.  
This lab prepares the environment for creating labeled datasets used in downstream OpenShift AI workflows.

---

## Optional advanced topics

Some labs include optional exercises that reflect real-world enterprise environments, such as:

- Identity integration and migration patterns
- FIPS enablement considerations
- Operational hardening and validation

These sections are clearly marked and scoped so they can be skipped without impacting the core lab flow.

---

## Audience

This repository is intended for:

- Platform engineers
- Solutions architects
- Public sector practitioners
- Red Hat partners and customers
- Anyone building or evaluating OpenShift AI workflows

---

## About Turtini

This repository is published by **Turtini**, a Red Hat partner focused on practical enablement, automation, and operational clarity in complex environments.

All content is provided as-is for educational and reference purposes.

---

## Contributing

Issues and pull requests are welcome where they improve clarity, correctness, or usability of the labs.

Please keep contributions focused on:
- Reproducibility
- Clear validation steps
- Alignment with supported OpenShift and OpenShift AI workflows
