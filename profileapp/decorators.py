
from django.http import HttpResponseForbidden
from profileapp.models import Profile


def pf_ownership_required(func):
    def decorated(request, *args, **kwargs):
        #본인인증 확인하는 과정
        user = Profile.objects.get(pk=kwargs['pk'])  #urls에서 받는 pk가 프로필의 주인을 확인
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated