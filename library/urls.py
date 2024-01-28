from django.urls import path

from .views import KitobListView

urlpatterns = [
    path('', KitobListView.as_view(), name='home')
]