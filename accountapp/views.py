from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import acc_ownership_required
from accountapp.forms import AccUpdateForm
from accountapp.models import HelloWorld
from django.http import HttpResponse, HttpResponseRedirect
#from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from articleapp.models import Article

has_ownership = [acc_ownership_required, login_required] # 이 배열 안에 있는 decorator들을 모두 확인해줌 -> 코드 2줄로 줄임

@login_required
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

class AccCreate(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')  # 계정 만드는 것에 성공했다면 어느 경로로 다시 연결해야할지
    #reverse(함수에서 사용) vs reverse_lazy(클래스에서 사용)
    template_name = 'accountapp/create.html' # 회원가입을 할 때 어느 html파일을 이용해서 볼지


class AccDetail(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
    pagination_by = 8

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccDetail, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccUpdate(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccUpdateForm  #UserCreationForm을 상속받아서 customize해줌 -> forms.py
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccDelete(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'