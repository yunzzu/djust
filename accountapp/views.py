
from django.shortcuts import render
from accountapp.models import HelloWorld
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        nhw = HelloWorld()  #models.py
        nhw.text = temp
        nhw.save()

        hello_world_list = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})