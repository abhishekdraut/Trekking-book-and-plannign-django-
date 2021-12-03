from django.db import models
from django.contrib.auth.models import User

# Create your models here.
days_choice=[('One day','One day'),('Two days One night','Two days One night')]
packages=[(1000,1000),(2000,2000)]
offer=[(10,10),(20,20),(30,30),(50,50)]
class contactus(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    image=models.ImageField(upload_to="uploaded_content")
    mobile=models.IntegerField()

class UserDetails(models.Model):
    User=models.ForeignKey(User,related_name="users",on_delete=models.SET_NULL,null=True)
    Address = models.CharField(max_length=200,null=False,blank=False)
    Mobile=models.CharField(max_length=12,null=False,blank=False)
    def __str__(self):
        return(self.User.first_name+" "+self.User.last_name)

class Destinations(models.Model):
    Name=models.CharField(max_length=100,null=False,blank=False)
    City=models.CharField(max_length=100,null=False,blank=False)
    State=models.CharField(max_length=100,null=False,blank=False)
    Offer=models.IntegerField(choices=offer,null=True)
    Img1=models.ImageField(max_length=100,null=True,blank=True)
    Img2=models.ImageField(max_length=100,null=True,blank=True)
    Img3=models.ImageField(max_length=100,null=True,blank=True)
    Img4=models.ImageField(max_length=100,null=True,blank=True)
    def __str__(self):
        return(self.Name)

class Days(models.Model):
    Days=models.CharField(max_length=50,choices=days_choice,default='one day')

    def __str__(self):
        return(self.Days)

class Package(models.Model):
    Days=models.ForeignKey(Days,related_name='packages',on_delete=models.SET_NULL,null=True)
    Package=models.IntegerField(choices=packages,null=False)
    
    def __str__(self):
        return(self.Days.Days)



class Invoice(models.Model):
    User=models.ForeignKey(User,related_name='invoice',on_delete=models.SET_NULL,default=None,null=True,blank=True)
    Destination=models.ForeignKey(Destinations,related_name='invoice',on_delete=models.SET_NULL,null=True)  
    Package=models.ForeignKey(Package,related_name='invoice',on_delete=models.SET_NULL,null=True) 
    Total=models.IntegerField(null=True,blank=True)     
    def __str__(self):
        return(self.Destination.Name)

class DetinationDetails(models.Model):
    Destination=models.ForeignKey(Destinations,related_name='destination_detail',on_delete=models.CASCADE)
    Short_description:models.TextField(blank=False)
    description=models.TextField(blank=False)
    Route=models.TextField(blank=False)
    Best_period=models.TextField(blank=False)

    def __str__(self):
        return(self.Destination.Name)

class RenderImage(models.Model):
    Img=models.ImageField(blank=True,null=True)
    status=models.BooleanField(default=True)
    def __str__(self):
        return("imgfile")