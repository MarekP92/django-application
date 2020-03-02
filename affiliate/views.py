from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post


class HomeView(TemplateView):
    template_name = 'home.html'

    def posts(self):
        return Post.objects.all()

def home(request):
    return render(request, 'home.html', {'posts': Post.objects.all()})
