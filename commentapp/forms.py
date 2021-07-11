
from django.forms import ModelForm
from commentapp.models import Comment

class CmCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']