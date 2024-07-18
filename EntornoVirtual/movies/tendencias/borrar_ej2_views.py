from django.shortcuts import render

# Create your views here.

def infoutil(request):
    infoutils = InfoUtil.objects.all()
    return render(request, "infoutil/infoutil.html", {'infoutils':infoutils})