from copy import error
from django.shortcuts import redirect, render
from  front.models import DetinationDetails, Package, contactus
from rest_framework import views,viewsets,status,response,permissions,serializers
from .import serializer 
from rest_framework.renderers import TemplateHTMLRenderer
from .import models as Allmodels
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.http import HttpResponse, JsonResponse
# Create your views here.




def bookpage(request):
    destinations=Allmodels.Destinations.objects.all()
    Package=Allmodels.Package.objects.all()
    
    
    if request.method == "POST":
        user=request.POST.get('user')
        package = request.POST.get('package')
        destination=request.POST.get("destination")
        print(package,destination,user)
        if package is None:
            messages.info(request,"Select the package")
        if destination is None:
            messages.info(request,'Destination Should not be empty')
        
        else:  
            Allmodels.Invoice.objects.create(Destination_id=destination,Package_id=package,User_id=user).save()
            
            destinationsDetails=Allmodels.Destinations.objects.get(id=destination)
            packagedetails=Allmodels.Package.objects.get(id=package)
            userdetails=Allmodels.User.objects.get(id=user)
            print(userdetails)
            if package=="1":
                total=[{'total':1000}]
            else:
                total=[{'total':2000}]
            print(total)
            return render(request,'done.html',{'destination':{destinationsDetails},'package':{packagedetails},'user':{userdetails},'total':total})
            
    return(render(request,'bookpage.html',{'destinations':destinations,'package':Package}))

def done(request):
    return render(request,'done.html')

def contact(request):
    if request.method=="POST":

        name1=request.POST["name"]
        address1=request.POST["address"]
        email1=request.POST["email"]
        img1=request.POST["image"]
        mobile1=request.POST["mobile"]

        contact=contactus()

        contact.name=name1
        contact.address=address1
        contact.email=email1
        contact.image=img1
        contact.mobile=mobile1
        contact.save()
        
        return(render(request,"contact.html"))




    return(render(request,"contact.html"))

class Home_page(viewsets.ViewSet):
    serializer_class=serializer.DestinationsModelserializer
    renderer_classes=[TemplateHTMLRenderer]
    template_name='index.html'

    def list(self,request):
        destinations=Allmodels.Destinations.objects.all()
        serialize=self.serializer_class(destinations,many=True)
        return(response.Response({'destinations':serialize.data}))
    
    def retrieve(self,request,pk=None):
        try:
            destination=Allmodels.Destinations.objects.get(id=pk)
            DestinationDetails=Allmodels.DetinationDetails.objects.get(Destination_id=pk)
            serialize=self.serializer_class(destination)
            render=Allmodels.RenderImage.objects.filter(status=True).order_by("?")
           
            render1={}
            for key, i in enumerate(render):
                render1[key]={
                    "img":i.Img.url,
                    "status":i.status,
                }
           
            render1=list(render1.values())
            print(render)
            print(render1)
            serialize=[{"one":serialize.data,"two":DestinationDetails}]
            print(serialize)
          
            
            return(response.Response({'destination':serialize,'render':render1},template_name="destinations.html"))
        except:
            return(response.Response("Object Not Found 404 ",status=status.HTTP_404_NOT_FOUND))





        


