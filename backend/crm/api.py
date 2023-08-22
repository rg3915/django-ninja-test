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

@router.put('customer/{customer_id}/', response=CustomerSchema)
def update_customer(request, customer_id: int, payload: CustomerSchemaIn):
    customer = Customer.objects.get(id=customer_id)
    for key, value in payload.dict().items():
        setattr(customer, key, value)
    customer.save()
    return customer

@router.delete('customer/{customer_id}/', response={HTTPStatus.NO_CONTENT: None})
def delete_customer(request, customer_id: int):
    customer = Customer.objects.get(id=customer_id)
    customer.delete()
    return None