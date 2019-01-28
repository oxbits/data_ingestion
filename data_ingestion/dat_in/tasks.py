from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import (
    Customer, 
    PurchaseType, 
    OrderRecord, 
)
from django.utils import dateparse
import decimal


@shared_task
def process_file(file_path):

    for line in open(file_path):
        values = line.split('\t')
        v = {
            'id': int(values[0]),
            'first_name': values[1], 
            'last_name': values[2], 
            'street_address': values[3], 
            'state': values[4],
            'zip_code': values[5],
            'purchase_status': values[6],
            'product_id': int(values[7]),
            'product_name': values[8],
            'purchase_amount': decimal.Decimal(values[9]),
            'date_time': dateparse.parse_datetime(values[10])
        }
        
        # does the customer exist? if not create.
        # if stored date is older, update it, else just get it

        customer, c_created = Customer.objects.get_or_create(
            id = v['id'],
            defaults={
                'first_name': v['first_name'], 
                'last_name': v['last_name'], 
                'street_address': v['street_address'], 
                'state': v['state'],
                'zip_code': v['zip_code'], 
                'date_time': v['date_time'],
            },
        )

        if not c_created and customer.date_time < v['date_time']:
            customer.first_name = v['first_name'] 
            customer.last_name = v['last_name']
            customer.street_address = v['street_address'] 
            customer.state = v['state']
            customer.zip_code = v['zip_code']
            customer.date_time = v['date_time']
            customer.save()

        # does purchase type exist?  if not create.  if yes get it

        purchase_type, p_created = PurchaseType.objects.get_or_create(
            product_id = v['product_id'], 
            product_name = v['product_name'], 
            purchase_amount = v['purchase_amount'], 
        )

        OrderRecord(
            customer = customer, 
            date_time = v['date_time'], 
            purchase_status = v['purchase_status'],
            purchase_type = purchase_type,
        ).save()

    return True
