from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import redirect
from check.models import MyEvent,Group
from django.http import JsonResponse



class HomeView(TemplateView):
    template_name = 'home.html'


class UserRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    # 타이밍 로딩 문제로 reverse를 사용시 에러가 발생
    success_url = reverse_lazy('register_done')


class UserRegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'

def myCheckEvent(request):
    user = request.user
    myEve = request.GET['eve']
    MyEvent.objects.create(usr=user, attend=myEve)
    myCount = MyEvent.objects.filter(usr=user, attend=myEve).count()
    laCount = MyEvent.objects.filter(usr=user, attend='LA').count()
    eaCount = MyEvent.objects.filter(usr=user, attend='EA').count()
    abCount = MyEvent.objects.filter(usr=user, attend='AB').count()
    ouCount = MyEvent.objects.filter(usr=user, attend='OU').count()
    result = {
        'myEve': myEve,
        'myCount': myCount,
        'laCount': laCount,
        'eaCount': eaCount,
        'abCount': abCount,
        'ouCount': ouCount,
    }
    return JsonResponse(result)

def removeEvent(request):
    user = request.user
    myReEve = request.GET['reve']
    q = MyEvent.objects.filter(usr=user, attend=myReEve).last()
    q= q.event_date
    delEve = MyEvent.objects.get(usr=user, attend=myReEve, event_date=q)
    delEve.delete()
    myCount = MyEvent.objects.filter(usr=user, attend=myReEve).count()
    laCount = MyEvent.objects.filter(usr=user, attend='LA').count()
    eaCount = MyEvent.objects.filter(usr=user, attend='EA').count()
    abCount = MyEvent.objects.filter(usr=user, attend='AB').count()
    ouCount = MyEvent.objects.filter(usr=user, attend='OU').count()
    result = {
        'myReEve':myReEve,
        'myCount':myCount,
        'laCount':laCount,
        'eaCount':eaCount,
        'abCount':abCount,
        'ouCount':ouCount
    }
    return JsonResponse(result)

def eventReset(request):
    user = request.user
    a = MyEvent.objects.filter(usr=user)
    a.delete()
    laCount = MyEvent.objects.filter(usr=user, attend='LA').count()
    eaCount = MyEvent.objects.filter(usr=user, attend='EA').count()
    abCount = MyEvent.objects.filter(usr=user, attend='AB').count()
    ouCount = MyEvent.objects.filter(usr=user, attend='OU').count()
    result = {
        'laCount': laCount,
        'eaCount': eaCount,
        'abCount': abCount,
        'ouCount': ouCount
    }
    return JsonResponse(result)


