# Lab 03: Train a Model with OpenShift AI

## Objective

In this lab, you will use **Red Hat OpenShift AI** to:

- Create a Data Science Project
- Launch a Workbench (Jupyter environment)
- Import a YOLO-formatted dataset
- Train a computer vision model
- Produce trained model artifacts

This lab builds directly on the dataset created in **Lab 02** and demonstrates a
realistic, end-to-end training workflow on OpenShift AI.

---

## Environment assumptions

This lab has been validated with:

- OpenShift Container Platform 4.20
- OpenShift AI 3.x
- CodeReady Containers (CRC) 2.48

Notes:
- **GPUs are optional**
- CPU-only execution is fully supported
- Git integration is optional
- Small datasets are sufficient for this lab

---

## What you will produce

By the end of this lab, you will have:

- A Data Science Project in OpenShift AI
- A running Workbench (Jupyter environment)
- A trained model artifact (weights/checkpoints)
- A repeatable workflow suitable for automation

---

## Step 1: Open the OpenShift AI dashboard

1. Log in to the OpenShift web console
2. From the application launcher (top-left), select **OpenShift AI**
3. Confirm you can access the OpenShift AI dashboard

---

## Step 2: Create a Data Science Project

1. In the OpenShift AI dashboard, navigate to **Data Science Projects**
2. Click **Create project**
3. Enter:
   - **Name:** `computer-vision-lab`
   - **Description:** `YOLO training with OpenShift AI`
4. Click **Create**

This project creates a dedicated namespace and resource boundary for your work.

---

## Step 3: Create a Workbench

1. Open the `computer-vision-lab` project
2. Navigate to **Workbenches**
3. Click **Create workbench**

### Workbench configuration

Use the following recommended settings:

- **Name:** `yolo-training`
- **Image:** PyTorch or general Python data science image
- **Deployment size:** Small or Medium
- **Persistent storage:** Enabled (10–20 GiB)

Optional (if available):
- **Accelerator:** GPU
- **Number of GPUs:** 1

Click **Create workbench** and wait for the status to become **Running**.

---

## Step 4: Launch the Workbench

1. Once the workbench is running, click **Open**
2. A Jupyter environment will open in a new browser tab

Confirm that you can create and run a notebook.

---

## Step 5: Import the YOLO dataset

Choose **one** of the following methods.

### Option A: Upload via Jupyter UI (simplest)

1. In Jupyter, click **Upload**
2. Upload the YOLO dataset archive from Lab 02
3. Extract it into your working directory

Expected structure:

```
dataset/

├── images/
├── labels/
└── classes.txt
```

---

### Option B: Copy from local system (optional)

If you prefer using the CLI:

```bash
oc rsync ./dataset computer-vision-lab:/opt/app-root/src/dataset
```

---

## Step 6: Prepare the training environment

Create a new notebook named:

```
train.ipynb
```

At a minimum, confirm required libraries are available. If needed, install them:

```
!pip install ultralytics torch torchvision
```

Note: CPU-only training will work but may take longer. GPU-backed workbenches
will train significantly faster.

---

## Step 7: Train the model

Example (YOLO-style) training workflow:

```
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.train(
    data="dataset",
    epochs=10,
    imgsz=640
)
```

Adjust parameters as needed:

- Reduce epochs for faster runs

- Increase epochs for better accuracy

- Use smaller images for CPU-only environments

Training output will be written to a runs/ directory.

---

## Step 8: Verify training output

Confirm that training artifacts exist:

```
runs/
└── detect/
    └── train/
        ├── weights/
        │   ├── best.pt
        │   └── last.pt
        └── results.png
```

These files represent the trained model and associated metrics.

---

## Step 9: Persist and export results

Because the workbench uses persistent storage:

- Model artifacts remain available after restarts

- Files can be downloaded directly from Jupyter

- Artifacts can be copied to object storage or Git (optional)

Example (optional):

```
oc rsync computer-vision-lab:/opt/app-root/src/runs ./runs
```

---

## Completion criteria

You have successfully completed this lab when:

- A Data Science Project exists in OpenShift AI

- A Workbench launches successfully

- The YOLO dataset is accessible in the workbench

- A training run completes without errors

- Model artifacts are produced and persisted

---

## Next steps

Possible follow-on activities include:

- Model evaluation and inference

- Serving the model using OpenShift AI

- Automating the workflow with Ansible

- Hardening identity, storage, and security controls

This concludes the core end-to-end OpenShift AI training workflow.
