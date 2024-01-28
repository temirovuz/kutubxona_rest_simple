from django.shortcuts import render
from django.views.generic import ListView

from library.models import Kitob


class KitobListView(ListView):
    model = Kitob
    template_name = 'home.html'