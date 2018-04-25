from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from .models import MyEvent,Group

# Create your views here.
class EventView(TemplateView):
    template_name = 'check/check_event.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        info = Group.objects.get(usr=user)
        context = super().get_context_data(**kwargs)
        context['user'] = user
        context['unit'] = info
        context['late'] = MyEvent.objects.filter(usr=user, attend='LA').count()
        context['earl'] = MyEvent.objects.filter(usr=user, attend='EA').count()
        context['absen'] = MyEvent.objects.filter(usr=user, attend='AB').count()
        context['out'] = MyEvent.objects.filter(usr=user, attend='OU').count()
        return context

