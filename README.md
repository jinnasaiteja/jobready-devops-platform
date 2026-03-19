# 🚀 DevOps End-to-End Project (FastAPI on AWS EKS)

## 📌 Overview
This project demonstrates a complete DevOps pipeline from application development to deployment and monitoring using modern cloud-native tools.

## 🧰 Tech Stack
- **Backend:** FastAPI (Python)
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Infrastructure:** Terraform (AWS)
- **Registry:** AWS ECR
- **Orchestration:** Kubernetes (EKS)
- **GitOps:** ArgoCD
- **Packaging:** Helm
- **Monitoring:** Prometheus & Grafana
- **Configuration Management:** Ansible

---

## ⚙️ Architecture
1. Developer pushes code to GitHub
2. GitHub Actions:
   - Builds Docker image
   - Pushes image to AWS ECR
3. ArgoCD:
   - Watches Git repo
   - Deploys Helm chart to EKS
4. Kubernetes:
   - Runs FastAPI app
   - Exposes via LoadBalancer
5. Prometheus & Grafana:
   - Collect and visualize metrics
6. Ansible:
   - Automates EC2 server setup (Docker, AWS CLI, tools)

---

## 🚀 Features
- Automated CI/CD pipeline
- Infrastructure as Code (Terraform)
- GitOps deployment using ArgoCD
- Helm-based Kubernetes packaging
- Auto-scaling via Kubernetes replicas
- Monitoring with Prometheus & Grafana
- Server provisioning with Ansible

---

## 📂 Project Structure
.
├── app/ # FastAPI application
├── k8s/ # Raw Kubernetes manifests
├── helm/fastapi-app/ # Helm chart
├── terraform/ # AWS infrastructure
├── ansible/ # Server automation
└── .github/workflows/ # CI/CD pipelines


---

## 🔍 Endpoints
- `/health` → Health check
- `/users` → User API

---

## 📊 Monitoring
- Prometheus metrics exposed at `/metrics`
- Grafana dashboards for visualization

---

## 🧪 CI/CD Flow
- Code push triggers GitHub Actions
- Image is built and pushed to ECR
- ArgoCD syncs and deploys automatically to EKS

---

## 🧠 Key Learnings
- Managing Kubernetes deployments with Helm
- Resolving conflicts between Helm and ArgoCD
- Implementing GitOps workflows
- Automating infrastructure with Terraform
- Using Ansible for server configuration
- Debugging real-world deployment issues

---

## 📬 Future Improvements
- Add autoscaling (HPA)
- Add ingress controller
- Add alerting in Prometheus
- Use secrets manager for credentials
