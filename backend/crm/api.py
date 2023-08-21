from typing import List
from ninja import Router
from ninja.orm import create_schema

from .models import Customer

router = Router()
CustomerSchema = create_schema(Customer)

@router.get('customer/', response=List[CustomerSchema])
def list_customer(request):
    return Customer.objects.all()