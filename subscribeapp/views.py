
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription

@method_decorator(login_required, 'get')
class SubView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk')) #project_pk를 가지고 있는 project를 찾고 없다면 404 response를 되돌려 줌
        user = self.request.user
        subscription = Subscription.objects.filter(user=user, project=project)

        if subscription.exists():  #구독 정보가 있다면 구독 정보를 없앰 (구독 취소)
            subscription.delete()
        else:  #구독 정보가 없다면 만듦
            Subscription(user=user, project=project).save()

        return super(SubView, self).get(request, *args, **kwargs)

@method_decorator(login_required, 'get')
class SubListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    #유저가 구독중인 프로젝트를 찾는함수
    def get_queryset(self):
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=projects)
        return article_list
