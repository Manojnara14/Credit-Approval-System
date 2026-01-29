
from rest_framework.decorators import api_view
from rest_framework.response import Response
from customers.models import Customer
from .models import Loan
from .utils import calculate_emi, credit_score

@api_view(['POST'])
def check_eligibility(request):
    c = Customer.objects.get(id=request.data['customer_id'])
    score = credit_score(c)
    approved = score > 30
    rate = request.data['interest_rate']
    if score <= 30: rate = 16
    emi = calculate_emi(request.data['loan_amount'], rate, request.data['tenure'])
    return Response({
        'customer_id': c.id,
        'approval': approved,
        'interest_rate': request.data['interest_rate'],
        'corrected_interest_rate': rate,
        'tenure': request.data['tenure'],
        'monthly_installment': emi
    })

@api_view(['POST'])
def create_loan(request):
    c = Customer.objects.get(id=request.data['customer_id'])
    emi = calculate_emi(request.data['loan_amount'], request.data['interest_rate'], request.data['tenure'])
    loan = Loan.objects.create(customer=c, loan_amount=request.data['loan_amount'],
        interest_rate=request.data['interest_rate'], tenure=request.data['tenure'],
        monthly_installment=emi)
    return Response({'loan_id': loan.id, 'loan_approved': True, 'monthly_installment': emi})

@api_view(['GET'])
def view_loan(request, loan_id):
    l = Loan.objects.get(id=loan_id)
    return Response({
        'loan_id': l.id,
        'customer': {
            'id': l.customer.id,
            'first_name': l.customer.first_name,
            'last_name': l.customer.last_name,
            'phone_number': l.customer.phone_number,
            'age': l.customer.age
        },
        'loan_amount': l.loan_amount,
        'interest_rate': l.interest_rate,
        'monthly_installment': l.monthly_installment,
        'tenure': l.tenure
    })

@api_view(['GET'])
def view_loans(request, customer_id):
    loans = Loan.objects.filter(customer_id=customer_id)
    return Response([{
        'loan_id': l.id,
        'loan_amount': l.loan_amount,
        'interest_rate': l.interest_rate,
        'monthly_installment': l.monthly_installment,
        'repayments_left': l.tenure
    } for l in loans])
