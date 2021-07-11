
from django.http import HttpResponseForbidden
from commentapp.models import Comment


def cm_ownership_required(func):
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        if not comment.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated