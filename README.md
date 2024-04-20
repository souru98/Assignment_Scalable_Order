# Order Service

## Overview
This repository contains the code for the Order Service, a part of a microservices architecture application. The Order Service is responsible for managing the orders in a book rental system.

## Features
- Issue a book
- Return an order
- Fetch all orders

## Technologies Used
- Flask: A lightweight WSGI web application framework.
- SQLAlchemy: The Python SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- Docker: A platform to develop, ship, and run applications inside containers.
- PostgreSQL: An open-source relational database management system (RDBMS).

## Getting Started

### Prerequisites
- Docker
- MiniKube
- Python 3.x
- PostgreSQL


### Steps to Configure and Use
1. **Clone the repository**
   ```
   git clone https://github.com/souru98/Assignment_Scalable_Order.git
2. **Create a virtual environment**
   ```
   python3 -m venv env source env/bin/activate
3. **Install the packages listed in the requirements.txt file**
   ```
   pip install -r requirements.txt
4. **Build and run the Docker container**
   ```
   docker compose up --build flask_order_service_app

## Deploying to MiniKube

Follow these steps to deploy your application to MiniKube:

1. **Navigate to Project Directory**: 
   Open Windows PowerShell and navigate to your project directory using the `cd` command.

2. **Start MiniKube**: 
   Start your MiniKube cluster with the command `minikube start`.

3. **Set Docker Environment**: 
   Set up the Docker environment inside MiniKube. Run the following command in PowerShell:
   ```powershell
   minikube -p minikube docker-env --shell powershell | Invoke-Expression
   
4. **Build Docker Image**
   ```powershell
   docker build -t order_service/flask_api:1.0 .
   
5. **Create Kubernetes Deployment**
   ```powershell
   kubectl run order-service-mk --image=order_service/flask_api:1.0 --image-pull-policy=Never --port=3000
   
6. **Port Forwarding**
   ```powershell
   kubectl port-forward order-service-mk 3000


## API Endpoints
- `/orders`: Issue a book
- `/orders/<int:order_id>`: Return an order
- `/orders`: Fetch all orders

## Dependencies
This service depends on the following services:
- Product Service (https://github.com/souru98/Assignment_Scalable_Product.git)
- User Service (https://github.com/souru98/Assignment_Scalable_User.git

Please ensure these services are up and running before starting the Order Service.

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

