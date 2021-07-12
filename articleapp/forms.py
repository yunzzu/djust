
from django.forms import ModelForm
from articleapp.models import Article


class AcCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
