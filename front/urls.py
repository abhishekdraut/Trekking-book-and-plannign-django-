from django.contrib import admin
from django.urls import path
from django.urls.conf import include 
from front import views
from rest_framework import routers
destinations_router=routers.DefaultRouter()
destinations_router.register("travello",views.Home_page,basename="destinations")

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("contact",views.contact,name="contactus"),
    path("invoice/",views.bookpage,name="invoicepage"),
    path("",include(destinations_router.urls)),
    path("travello/",views.Home_page.as_view({'get': 'retrieve'}),name="alldestination"),
    path("travello/<int:pk>",views.Home_page.as_view({'get': 'retrieve'}),name="destination"),
    path("done/",views.done,name="done"),
    
   
]
