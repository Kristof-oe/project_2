## Project overview
This projects demonstrates end-to-end DevOps workflow built around FastApi backend service, including databse model, http request and http input. In additional, this project has monitoring and argocd too. This main goal is automated build, test and deployment process using Jenkins, Docker, Helm and Kubernetes, including Prometheus/Grafana and ArgoCD as well

This app itself is simply focusing on CI/CD pipeline and infrastructure automation

- **FastApi** - Backend REST API with SQL model
- **Jenkins** - CI orchestration
- **Docker** - Application containerization
- **Helm** - Kubernetes package management
- **Kubernetes (kind)** – Local Kubernetes cluster for deployment and testing
- **PostgreSQL** - Used bitnami for DB setting for FastApi
- **Prometheus/Grafana** - Monitoring http for more security
- **ArgoCD** - Pushed github automatically refresh the state of kubernetes and making CD orchestration

***Github Push --> Jenkins pipeline (CI) and ArgoCD (CD)***

-  **Jenkins**
    -  Clone
    -  Setup env
    -  Test unit
    -  Build local
    -  Smoke test locally
    -  Cleanup
    -  Login docker
    -  Push image

-   **ArgoCD**
    -   Deploy fastapi postgresql and grafana/prometheus by helm