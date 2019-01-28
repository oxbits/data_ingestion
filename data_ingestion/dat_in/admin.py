from django.contrib import admin
from .models import (
    DataFile,
    Customer, 
    PurchaseType, 
    OrderRecord, 
)
from django import forms


class UploadFileModelForm(forms.ModelForm):
    class Meta:
        model = DataFile
        exclude = []


class UploadFileModelAdmin(admin.ModelAdmin):
    change_form_template = 'progressbarupload/change_form.html'
    add_form_template = 'progressbarupload/change_form.html'
    form = UploadFileModelForm

    class Media:
        js = ("http://code.jquery.com/jquery.min.js",)


admin.site.register(DataFile, UploadFileModelAdmin)
admin.site.register(Customer)
admin.site.register(PurchaseType)
admin.site.register(OrderRecord)
