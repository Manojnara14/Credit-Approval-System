# Credit Approval System

A backend Credit Approval System built using Django REST Framework as part of a backend internship assignment.

---

## Features

- Register new customers
- Check loan eligibility based on credit score logic
- Create loans for eligible customers
- View loan details by loan ID
- View all loans for a customer
- Fully dockerized with PostgreSQL

---

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose

---

## How to Run

### Prerequisites
- Docker
- Docker Compose

### Steps

git clone https://github.com/Manojnara14/Credit-Approval-System.git  
cd Credit-Approval-System  
docker-compose up --build  

---

## API Endpoints

POST /register  
POST /check-eligibility  
POST /create-loan  
GET /view-loan/<loan_id>  
GET /view-loans/<customer_id>

---

## Demo Video

https://drive.google.com/file/d/1-k-AVTCFWzfr3vkVMkX_KGQYZMLyXQV8/view?usp=drive_link

---

## Author

Manoj Nara
