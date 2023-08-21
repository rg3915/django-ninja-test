from typing import List
from ninja import Router, ModelSchema
from ninja.orm import create_schema
from http import HTTPStatus

from .models import Customer

router = Router()
CustomerSchema = create_schema(Customer)

class CustomerSchemaIn(ModelSchema):
    class Config:
        model = Customer
        model_fields = (
            'name',
        )

@router.get('customer/', response=List[CustomerSchema])
def list_customer(request):
    return Customer.objects.all()

@router.post('customer/', response={HTTPStatus.CREATED: CustomerSchema})
def create_customer(request, payload: CustomerSchemaIn):
    return Customer.objects.create(**payload.dict())