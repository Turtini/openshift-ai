# Lab 04: Model Serving and Inference with OpenShift AI

## Objective

In this lab, you will deploy a trained model using **Red Hat OpenShift AI** and perform
inference against it.

By the end of this lab, you will:

- Register a trained model
- Deploy a model serving endpoint
- Perform inference using sample inputs
- Validate end-to-end model accessibility

This lab builds on the model artifacts created in **Lab 03** and demonstrates how trained
models are exposed for consumption in real environments.

---

## Environment assumptions

This lab has been validated with:

- OpenShift Container Platform 4.20
- OpenShift AI 3.x
- CodeReady Containers (CRC) 2.48

Notes:
- GPU acceleration is **optional**
- CPU-only model serving is fully supported
- This lab uses OpenShift AI’s **model serving abstractions**
- External authentication is not required for this lab

---

## What you will produce

By the end of this lab, you will have:

- A registered model in OpenShift AI
- A deployed inference service
- A reachable REST endpoint
- Successful inference responses

---

## Step 1: Verify model artifacts

Ensure you have completed **Lab 03** and that trained model artifacts exist.

In your OpenShift AI workbench, confirm files similar to:

```
runs/
└── detect/
└── train/
└── weights/
└── best.pt
```

This file will be used for model serving.

---

## Step 2: Register the model

1. Open the **OpenShift AI** dashboard
2. Navigate to your **Data Science Project**
3. Select **Models**
4. Click **Register model**

Enter the following:

- **Model name:** `yolo-object-detector`
- **Model framework:** PyTorch
- **Model location:** Path to your model artifact (for example):

```
/opt/app-root/src/runs/detect/train/weights/best.pt
```


Click **Register**.

---

## Step 3: Deploy a model server

1. In the OpenShift AI dashboard, navigate to **Model servers**
2. Click **Deploy model server**

### Model server configuration

Use the following recommended values:

- **Model name:** `yolo-object-detector`
- **Serving runtime:** PyTorch
- **Deployment size:** Small
- **Replicas:** 1

Optional:
- Enable GPU acceleration if available

Click **Deploy** and wait for the model server status to become **Ready**.

---

## Step 4: Verify the inference service

Once deployed:

1. Navigate to **Inference endpoints**
2. Select the deployed endpoint
3. Note the **REST endpoint URL**

This endpoint will be used to submit inference requests.

---

## Step 5: Perform inference

### Option A: Use curl (example)

Prepare a sample image encoded as base64 or referenced by path, depending on the serving
runtime configuration.

Example request structure:

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
      "inputs": [
        {
          "name": "image",
          "shape": [1],
          "datatype": "BYTES",
          "data": ["<base64-encoded-image>"]
        }
      ]
    }' \
<INFERENCE_ENDPOINT_URL>
```

### Option B: Perform inference from a notebook

From your OpenShift AI workbench:

```
import requests

url = "<INFERENCE_ENDPOINT_URL>"

payload = {
    "inputs": [
        {
            "name": "image",
            "shape": [1],
            "datatype": "BYTES",
            "data": ["<base64-encoded-image>"]
        }
    ]
}

response = requests.post(url, json=payload)
print(response.json())
```

---

## Step 6: Interpret results

A successful response typically includes:

- Detection results

- Bounding box coordinates

- Confidence scores

Exact output depends on the model runtime and configuration, but a valid JSON response
indicates successful inference.

---

## Step 7: Validate persistence and availability

Confirm:

- The inference service remains available after refresh

- The endpoint remains reachable

- Logs show successful request handling

You may inspect logs via:

- OpenShift web console → Pods → Logs

---

## Completion criteria

You have successfully completed this lab when:

- A trained model is registered in OpenShift AI

- A model server is deployed and Ready

- An inference endpoint is available

- Inference requests return valid responses

---

## Next steps

In the next lab, you will:

- Automate the end-to-end workflow using Ansible

- Provision projects, workbenches, and model servers programmatically

Proceed to Lab 05: Automating OpenShift AI workflows with Ansible.
