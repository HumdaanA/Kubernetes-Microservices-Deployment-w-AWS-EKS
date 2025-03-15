# Kubernetes Microservices Project on AWS EKS w/ JWT Authentication

## Project Overview

This project demonstrates a complete microservices architecture deployed on AWS Elastic Kubernetes Service (EKS). The application consists of three main components: an authentication service, a backend service, and a frontend React application. JWT (JSON Web Token) authentication secures the services, ensuring that only authenticated users can access protected resources.

## Architecture Diagram

```
[ User ] <--> [ Frontend (React) ] <--> [ AWS Load Balancer ] <--> [ Auth Service | Backend Service ]
                                               |                          |
                                         [ EKS Cluster ]            [ EKS Cluster ]
```

## Tech Stack

- **AWS EKS**: Managed Kubernetes service for scalable deployments

- **Terraform**: Infrastructure as Code (IaC) for AWS resource provisioning

- **Docker**: Containerization of services

- **React**: Frontend with user authentication

- **FastAPI**: Backend service and authentication

- **JWT**: JSON Web Token for secure communication


## Features

- User authentication with JWT

- Secure access to protected backend services

- Scalable deployment on AWS EKS using Terraform

- CI/CD pipeline with GitHub Actions


### Contact

Humdaan Ahmad || [LinkedIn](https://www.linkedin.com/in/ahumdaan) || [Portfolio](https://www.humdaan-ahmad-portfolio.com)

