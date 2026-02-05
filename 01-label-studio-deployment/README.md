# Lab 01: Deploy Label Studio on OpenShift

## Objective

In this lab, you will deploy **Label Studio** on Red Hat OpenShift using a standard,
production-aligned pattern:

- Deployment
- PersistentVolumeClaim (PVC)
- Service
- Route

By the end of this lab, you will have a persistent, browser-accessible Label Studio
instance that can be used to create labeled datasets for downstream **OpenShift AI**
training workflows.

This lab is intentionally **console-first** and designed to work in lightweight
environments such as CodeReady Containers (CRC).

---

## Environment assumptions

This lab has been validated with:

- OpenShift Container Platform 4.20
- CodeReady Containers (CRC) 2.48
- OpenShift AI 3.x (used in later labs)

Notes:
- GPUs are **not required**
- Git integration is **not required**
- CPU-only execution paths are fully supported

---

## What you will deploy

This lab deploys:

- A single-instance Label Studio application
- Persistent storage for application data
- An externally accessible HTTPS route

The architecture follows common OpenShift patterns and is intentionally simple so it
can be reproduced and adapted easily.

---

## Step 1: Create a project (namespace)

1. Log in to the OpenShift web console
2. Navigate to **Home → Projects**
3. Click **Create Project**
4. Enter:
   - **Name:** `label-studio`
5. Click **Create**

All remaining steps in this lab occur in the `label-studio` project.

---

## Step 2: Deploy Label Studio resources

This step creates all required resources in a single action.

### Apply the manifest

1. Navigate to **+Add → Import YAML**
2. Paste the following manifest
3. Click **Create**

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: label-studio-data
  namespace: label-studio
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: label-studio
  namespace: label-studio
  labels:
    app: label-studio
spec:
  replicas: 1
  selector:
    matchLabels:
      app: label-studio
  template:
    metadata:
      labels:
        app: label-studio
    spec:
      containers:
        - name: label-studio
          image: heartexlabs/label-studio:latest
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 8080
              name: http
          env:
            - name: LABEL_STUDIO_BASE_DATA_DIR
              value: /data
            - name: LABEL_STUDIO_HOST
              value: "0.0.0.0"
            - name: LABEL_STUDIO_PORT
              value: "8080"
          volumeMounts:
            - name: data
              mountPath: /data
          resources:
            requests:
              cpu: "250m"
              memory: "512Mi"
            limits:
              cpu: "1"
              memory: "2Gi"
          readinessProbe:
            httpGet:
              path: /
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 10
          livenessProbe:
            httpGet:
              path: /
              port: 8080
            initialDelaySeconds: 30
            periodSeconds: 20
      volumes:
        - name: data
          persistentVolumeClaim:
            claimName: label-studio-data
---
apiVersion: v1
kind: Service
metadata:
  name: label-studio
  namespace: label-studio
  labels:
    app: label-studio
spec:
  selector:
    app: label-studio
  ports:
    - name: http
      port: 80
      targetPort: 8080
---
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: label-studio
  namespace: label-studio
  labels:
    app: label-studio
spec:
  to:
    kind: Service
    name: label-studio
  port:
    targetPort: http
  tls:
    termination: edge
```

---

## Step 3: Verify the deployment

1. Navigate to Topology

2. Confirm the label-studio application appears

3. Select the application and open the Resources tab

4. Verify:

- One pod is running

- The pod reaches a Ready state

---

## Step 4: Access Label Studio

1. Navigate to Networking → Routes

2. Click the label-studio route

3. Open the Location URL in your browser

On first access, you should see the Label Studio UI and be prompted to create an
administrator account.

---

## Step 5: Verify persistent storage

Verify the PVC is bound

1. Navigate to Storage → PersistentVolumeClaims

2. Confirm label-studio-data shows a status of Bound
   

Verify data persistence across restarts

1. Navigate to Workloads → Pods

2. Select the Label Studio pod

3. Click Actions → Delete Pod

4. Wait for the pod to be recreated

5. Refresh the Route URL and confirm the application still loads correctly

This confirms that application data is stored on the PVC.

---

## Troubleshooting: Permission errors on OpenShift

Some third-party container images are not compatible with OpenShift’s default restricted
security context.

If the pod enters CrashLoopBackOff and logs indicate permission errors writing to
/data, you may apply the following non-production workaround:

```yaml
oc project label-studio
oc adm policy add-scc-to-user anyuid -z default
oc rollout restart deployment/label-studio
```

After the rollout restart, verify the pod reaches a Ready state.

In production environments, a hardened image or adjusted security context should be
used instead of granting the ```yaml anyuid``` SCC.

---

## Completion criteria

You have successfully completed this lab when:

- The Label Studio route is reachable in a browser

- The Label Studio pod is running and Ready

- The PersistentVolumeClaim is bound

- Restarting the pod does not result in data loss

---

## Next steps

In the next lab, you will use Label Studio to:

- Create a labeling project

- Label sample images

- Export the dataset in YOLO format

That dataset will be used in subsequent OpenShift AI training exercises.
