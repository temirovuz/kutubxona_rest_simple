from rest_framework import generics

from api.serializers import KitobSerializer
from library.models import Kitob


# list api
class KitobAPIView(generics.ListAPIView):
    queryset = Kitob.objects.all()
    serializer_class = KitobSerializer


class KitobCreateView(generics.CreateAPIView):
    queryset = Kitob.objects.all()
    serializer_class = KitobSerializer


# update api
class KitobDetailView(generics.RetrieveUpdateAPIView):
    queryset = Kitob
    serializer_class = KitobSerializer


# delete api
class KitobDetailDeleView(generics.RetrieveDestroyAPIView):
    queryset = Kitob
    serializer_class = KitobSerializer


# create list api
class KitobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kitob.objects.all()
    serializer_class = KitobSerializer


# update delete, detail
class KitobDetailDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitob
    serializer_class = KitobSerializer
