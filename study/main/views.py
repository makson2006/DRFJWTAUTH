from .models import Men
from rest_framework import generics
from .serializers import MenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class MenAPIView(generics.ListCreateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAuthenticated, )

class MenRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAuthenticated, )
