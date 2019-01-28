from django.db import models


class DataFile(models.Model):
    data_file = models.FileField()

    def __str__(self):
        return ' '.join((
            str(self.data_file),
        ))


class Customer(models.Model):
    first_name = models.CharField(null=True, default='', max_length=100, )
    last_name = models.CharField(null=True, default='', max_length=100, )
    street_address = models.CharField(null=True, default='', max_length=100, )
    state = models.CharField(null=True, default='', max_length=100, )
    zip_code = models.CharField(null=True, default='', max_length=100, )
    date_time = models.DateTimeField(null=True, )

    def __str__(self):
        return ' '.join((
            self.first_name,
            self.last_name,
        ))


class PurchaseType(models.Model):
    product_id = models.IntegerField(null=True, )
    product_name = models.CharField(null=True, default='', max_length=100, )
    purchase_amount = models.DecimalField(null=True, max_digits=6, decimal_places=2, )

    class Meta:
        unique_together = (('product_id', 'product_name', 'purchase_amount', ), )

    def __str__(self):
        return ' '.join((
            str(self.product_id), 
            self.product_name,
            '$' + str(self.purchase_amount),
        ))

    


class OrderRecord(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, )
    date_time = models.DateTimeField(null=True, )
    purchase_status = models.CharField(null=True, default='', max_length=8, )
    purchase_type = models.ForeignKey(PurchaseType, on_delete=models.CASCADE, )

    def __str__(self):
        return ' '.join((
            str(self.date_time), 
            self.purchase_status, 
            self.customer.first_name, 
            self.customer.last_name,
            str(self.purchase_type.product_id), 
            self.purchase_type.product_name,
            str(self.purchase_type.purchase_amount),
        ))
