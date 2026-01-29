
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer

@api_view(['POST'])
def register(request):
    income = request.data['monthly_income']
    approved = round((36 * income) / 100000) * 100000
    customer = Customer.objects.create(
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        age=request.data['age'],
        phone_number=request.data['phone_number'],
        monthly_income=income,
        approved_limit=approved
    )
    return Response(CustomerSerializer(customer).data, status=201)
