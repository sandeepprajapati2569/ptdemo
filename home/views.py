from django.shortcuts import render,redirect
from home.models import url
# Create your views here.
def home(request):
    x=url.objects.all()
    return render(request,'home.html',{'x':x})

def url_save(request):
    url1=request.POST['url_val']
    x=url(url=url1)
    x.save()
    return redirect("http://127.0.0.1:8000/")