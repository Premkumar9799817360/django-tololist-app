from django.shortcuts import render , HttpResponse
from .models import Storage
from math import ceil
# Create your views here.
def index(request):
    bom = Storage.objects.all()
    print(bom)
    # n= len(bom)
    # nSlides= n//4 + ceil((n/4) + (n//4))
    params={ 'range':range(1,), 'bom': bom}
    # params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'bom': bom}
    print(bom)
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        city = request.POST.get('city')
        email = request.POST.get('email')
        prem = Storage(name=name, mobile= mobile,email= email, city=city)
        prem.save()
    return render(request, 'index.html',params)

def chack(request):
    return HttpResponse("successfuly connected")