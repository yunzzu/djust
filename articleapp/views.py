from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from articleapp.decorators import ac_ownership_required
from django.contrib.auth.decorators import login_required
from articleapp.forms import AcCreationForm
from articleapp.models import Article


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AcCreateView(CreateView):
    model = Article
    form_class = AcCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form): #writer값을 서버에 지정해주기 위함
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


class AcDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'

@method_decorator(ac_ownership_required, 'get')
@method_decorator(ac_ownership_required, 'post')
class AcUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = AcCreationForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(ac_ownership_required, 'get')
@method_decorator(ac_ownership_required, 'post')
class AcDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'


class AcListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 8