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
- Python 3.x
- PostgreSQL


### Steps to Configure and Use
1. **Clone the repository**
   git clone https://github.com/souru98/Assignment_Scalable_Order.git
2. **Create a virtual environment**
   python3 -m venv env source env/bin/activate
3. **Install the packages listed in the requirements.txt file**
   pip install -r requirements.txt
4. **Build and run the Docker container**
   docker compose up --build flask_product_service_app


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

