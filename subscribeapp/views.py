from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import RedirectView

from projectapp.models import Project
from subscribeapp.models import Subscription


class SubView(RedirectView):
    def get_redirect_view(self):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project.pk')})
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk')) #project_pk를 가지고 있는 project를 찾고 없다면 404 response를 되돌려 줌
        user = self.request.user
        subscription = Subscription.objects.filter(user=user, project=project)

        if subscription.exists():  #구독 정보가 있다면 구독 정보를 없앰 (구독 취소)
            subscription.delete()
        else:  #구독 정보가 없다면 만듦
            Subscription(user=user, project=project).save()

        return super(SubView, self).get(request, *args, **kwargs)

