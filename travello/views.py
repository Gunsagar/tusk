
from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dests=Destination.objects.all()
    #dest1=Destination()
    #dest1.name='Mumbai'
    #dest1.desc="city that never sleeps"
    #dest1.price=800
    #dest1.img='destination_1.jpg'
    #dest1.offer=True
    #dest2=Destination()
    #dest2.name='Delhi'
    #dest2.desc="IIT"
    #dest2.price=400
    #dest2.img='destination_2.jpg'
    #dest2.offer=True
    #dest3=Destination()
    #dest3.name='Ldh'
    #dest3.desc="Home"
    #dest3.price=200
    #dest3.img='destination_3.jpg'
   
    #dest3.offer=False
    #dests=[dest1,dest2,dest3]

    return render(request,'index.html',{'dests': dests})
# Create your views here.
