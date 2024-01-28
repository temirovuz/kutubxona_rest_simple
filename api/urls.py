from django.urls import path

from api.views import (KitobAPIView, KitobCreateView, KitobDetailView, KitobDetailDeleView, KitobListCreateAPIView,
                       KitobDetailDeleteUpdateAPIView)

urlpatterns = [
    path('kitoblar/', KitobAPIView.as_view()),
    path('addlist/', KitobListCreateAPIView.as_view()),
    path('qoshish/', KitobCreateView.as_view()),
    path('update/<int:pk>', KitobDetailView.as_view()),
    path('delete/<int:pk>', KitobDetailDeleView.as_view()),
    path('delete-update/<int:pk>', KitobDetailDeleteUpdateAPIView.as_view()),
]