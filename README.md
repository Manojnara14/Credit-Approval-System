
# Credit Approval System – Backend Assignment

## How to Run
docker-compose up --build

## APIs
POST /register
POST /check-eligibility
POST /create-loan
GET  /view-loan/<loan_id>
GET  /view-loans/<customer_id>

## Notes
- Compound interest EMI used
- Credit score based approval
- Dockerized, PostgreSQL-backed
