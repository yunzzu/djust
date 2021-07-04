from django.http import HttpResponse
from django.shortcuts import render
from accountapp.models import HelloWorld

def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')
        nhw = HelloWorld()  #models.py
        nhw.text = temp
        nhw.save()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': temp})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD 🍸'})