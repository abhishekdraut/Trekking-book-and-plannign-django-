from rest_framework import fields, serializers
from .import models as Allmodels
from django.contrib.auth.models import User







class InvoiceModelserializer(serializers.ModelSerializer):
    class Meta:
        model=Allmodels.Invoice
        fields='__all__'
class UserModelserializer(serializers.ModelSerializer):
    invoice=InvoiceModelserializer(read_only=True,many=True)
    class Meta:
        model=User
        fields='__all__'      
class DestinationsModelserializer(serializers.ModelSerializer):
    invoice=InvoiceModelserializer(read_only=True,many=True)
    class Meta:
        model=Allmodels.Destinations
        fields='__all__'      
class PackageModelserializer(serializers.ModelSerializer):
    invoice=InvoiceModelserializer(read_only=True,many=True)
    class Meta:
        model=Allmodels.Package
        fields='__all__'              