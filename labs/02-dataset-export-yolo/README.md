# Lab 02: Create Labels and Export a YOLO Dataset with Label Studio

## Objective

In this lab, you will use **Label Studio** to:

- Create a computer vision labeling project
- Upload sample images
- Label objects using bounding boxes
- Export the labeled dataset in **YOLO format**

The resulting dataset will be used in subsequent labs to train a model using
**Red Hat OpenShift AI**.

---

## Environment assumptions

This lab assumes:

- Lab 01 has been completed successfully
- Label Studio is running and accessible via an OpenShift Route
- You can log in to the Label Studio UI

This lab has been validated with:

- OpenShift Container Platform 4.20
- CodeReady Containers (CRC) 2.48

Notes:
- GPUs are not required
- Git is optional
- Any small image dataset is sufficient for this lab

---

## What you will produce

By the end of this lab, you will have:

- A labeled image dataset
- A YOLO-formatted export containing:
  - `images/`
  - `labels/`
  - `classes.txt`

This directory structure is required by common YOLO training workflows.

---

## Step 1: Access Label Studio

1. Log in to the OpenShift web console
2. Navigate to **Networking → Routes**
3. Click the **label-studio** route
4. Log in to Label Studio using the administrator account you created in Lab 01

---

## Step 2: Create a new labeling project

1. From the Label Studio home screen, click **Create Project**
2. Enter the following:
   - **Project Name:** `object-detection-lab`
3. Click **Create**

---

## Step 3: Configure labeling interface (bounding boxes)

1. After creating the project, select **Labeling Setup**
2. Choose **Object Detection with Bounding Boxes**
3. Use a simple labeling configuration with one or more labels (for example):

   - `object`
   - `vehicle`
   - `person`

4. Save the labeling configuration

> Keep labels simple and lowercase. These names will appear in `classes.txt`
> in the YOLO export.

---

## Step 4: Upload images

1. Open the project
2. Click **Import**
3. Upload a small set of image files (JPEG or PNG)

Notes:
- A minimum of 5–10 images is sufficient for this lab
- Images can be any object-detection-friendly content
- Image size and resolution are not critical for this exercise

After upload, confirm the images appear in the task list.

---

## Step 5: Label images

1. Click an image to open the labeling interface
2. Draw bounding boxes around objects of interest
3. Assign the appropriate label to each bounding box
4. Save the annotation
5. Repeat for each image

Guidelines:
- Ensure at least one labeled object per image
- Use consistent labeling across all images
- Accuracy matters more than quantity for this lab

---

## Step 6: Export the dataset in YOLO format

1. From the project page, click **Export**
2. Select **YOLO** as the export format
3. Start the export
4. Download the resulting archive (ZIP file)

---

## Step 7: Inspect the exported dataset

Unzip the downloaded archive locally and confirm the following structure:

```
dataset/

├── images/
│ ├── image1.jpg
│ ├── image2.jpg
│ └── ...
├── labels/
│ ├── image1.txt
│ ├── image2.txt
│ └── ...
└── classes.txt
```

### Validate contents

- `images/` contains the original images
- `labels/` contains one `.txt` file per image
- Each label file includes bounding box coordinates in YOLO format
- `classes.txt` lists class names in index order

Example `classes.txt`:
object
vehicle
person

---

## Optional: Store the dataset for reuse

You may optionally store the exported dataset using one of the following methods:

- Keep it locally for upload into a Jupyter workbench
- Upload it to object storage (S3-compatible)
- Commit it to a Git repository (for small datasets only)

Git is optional and not required for subsequent labs.

---

## Completion criteria

You have successfully completed this lab when:

- A Label Studio project exists with labeled images
- The dataset has been exported in YOLO format
- The exported archive contains `images/`, `labels/`, and `classes.txt`
- The dataset is available locally or in a location accessible to OpenShift AI

---

## Next steps

In the next lab, you will:

- Create a **Data Science Project** in OpenShift AI
- Launch a **Workbench** (Jupyter environment)
- Import the YOLO dataset
- Train a model using **OpenShift AI**

Proceed to **Lab 03: Train a model with OpenShift AI**.
