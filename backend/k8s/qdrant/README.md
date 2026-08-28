# Qdrant Kubernetes Production Deployment

This directory contains the necessary Kubernetes manifests to deploy a production-ready, highly-available 3-node Qdrant cluster for ELARA.

## Deployment Instructions

1. **Create the Namespace:**
   ```bash
   kubectl apply -f namespace.yaml
   ```

2. **Configure Secrets:**
   Update `secret.yaml` with a secure API key (do NOT commit this change to source control) or use your preferred secret injection method (e.g., ExternalSecrets, SealedSecrets).
   ```bash
   kubectl apply -f secret.yaml
   ```

3. **Install the Qdrant Helm Chart:**
   Ensure you have the Qdrant helm repository added.
   ```bash
   helm repo add qdrant https://qdrant.to/helm
   helm repo update
   
   helm install elara-qdrant qdrant/qdrant \
     -n elara-qdrant \
     -f values-production.yaml \
     --version 0.7.2  # Matches application requirements
   ```

4. **Verify Deployment:**
   ```bash
   kubectl get statefulset -n elara-qdrant
   kubectl get pods -n elara-qdrant -w
   ```
