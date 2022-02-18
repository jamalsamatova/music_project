from rest_framework import generics

from applications.music.models import Music
from applications.music.serializers import MusicSerializer


class MusicListView(generics.ListAPIView):
    queryset = Music.objects.all()
    # псевдо список, в котором лежит объект от какой либо модели
    serializer_class = MusicSerializer
