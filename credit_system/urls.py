
from django.urls import path, include
urlpatterns = [
 path('', include('customers.urls')),
 path('', include('loans.urls')),
]
