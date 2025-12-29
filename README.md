# 🌐 Cloud Resume Challenge — Azure

Implementation of the **Cloud Resume Challenge (Azure edition)**.  
It demonstrates real-world cloud engineering skills using **Microsoft Azure**, **serverless architecture**, and **CI/CD automation**.

---

## 🚀 Live Demo

- **Resume Website:** https://crcresume123.z13.web.core.windows.net/  
- **Backend API:** https://ag-test2-dxd8f0b7freva6fp.canadacentral-01.azurewebsites.net/api/http_trigger

---

## 🧠 Architecture Overview

```

User Browser
↓
Static Resume (Azure Storage Static Website)
↓
JavaScript fetch()
↓
Azure Function (HTTP Trigger, Python)
↓
Azure Cosmos DB (NoSQL)

```

### How it works
- The resume is hosted as a **static website** on Azure Storage.
- On page load, JavaScript calls an **HTTP-triggered Azure Function**.
- The function reads a visitor counter from **Cosmos DB**, increments it, and returns the updated value.
- The frontend displays the live visitor count.

---

## 🏗️ Tech Stack

### Frontend
- HTML, CSS, JavaScript
- Azure Storage (Static Website Hosting)

### Backend
- Azure Functions (Python, v2 programming model)
- Azure Cosmos DB (NoSQL, Serverless)

### DevOps / CI-CD
- GitHub Actions
- Azure ZIP Deploy (Kudu)
- Secrets managed via GitHub repository secrets

---

## 📁 Repository Structure

```

.
├── crc-frontend/
│   ├── index.html
│   └── style.css
│
├── crc-function-backend/
│   ├── function_app.py
│   ├── host.json
│   ├── requirements.txt
│   └── .funcignore
│
├── .github/
│   └── workflows/
│       ├── frontend.yml
│       └── backend.yml
│
└── README.md

```

---

## 🔄 CI/CD Pipelines

### Frontend Pipeline
- Triggered on changes to `crc-frontend/**`
- Uploads static files to Azure Storage `$web` container

### Backend Pipeline
- Triggered on changes to `crc-function-backend/**`
- Deploys Python Azure Function via ZIP deploy
- Uses secure publish profile authentication

Both pipelines support **manual execution** via `workflow_dispatch`.

---

## 🔐 Security & Configuration

- No secrets committed to the repository
- Sensitive values stored in **GitHub Secrets**
- Azure Function uses **Application Settings** for Cosmos DB credentials
- `.funcignore` ensures only required files are deployed

---

## 🧪 Key Learnings & Challenges Solved

- Azure Functions Python v2 deployment model
- Debugging Kudu (SCM) authentication errors
- Handling `.funcignore` deployment exclusions
- Understanding cold starts and function discovery
- Building a monorepo with isolated CI/CD workflows
- Secure secret management in CI/CD pipelines

---

## 📌 Cloud Resume Challenge Requirements

✔ Static website hosted on Azure  
✔ HTTPS enabled  
✔ Visitor counter backed by a database  
✔ Serverless backend API  
✔ CI/CD for frontend and backend  
✔ Source code publicly available  

---

## 🧩 Future Improvements

- Infrastructure as Code (Bicep / ARM)
- Entra ID (OIDC) authentication for deployments
- Application Insights monitoring
- Rate limiting / API protection
- Custom domain with Azure CDN

---

## 👤 Author

**Abhishek Gaurav**  
Cloud / DevOps Engineer  

- GitHub: https://github.com/ag9ggaurav  
- LinkedIn: https://www.linkedin.com/in/abhishek-gaurav-aa87a61b4/

---

## 📜 Acknowledgements

- Cloud Resume Challenge by Forrest Brazeal  
- Microsoft Azure documentation & community
```
