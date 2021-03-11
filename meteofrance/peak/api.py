from rest_framework import generics
from rest_framework.response import Response
from .serializer import PeakSerializer
from .models import Peak


class GetPeaks(generics.ListAPIView):
    queryset = Peak.objects.all()
    serializer_class = PeakSerializer

class GetPeaksByBoundingBox(generics.ListAPIView):
    queryset = Peak.objects.all()
    serializer_class = PeakSerializer

class CreatePeak(generics.CreateAPIView):
    queryset = Peak.objects.all()
    serializer_class = PeakSerializer

class UpdatePeak(generics.RetrieveUpdateAPIView):
    queryset = Peak.objects.all()
    serializer_class = PeakSerializer

class DeletePeak(generics.DestroyAPIView):
    queryset = Peak.objects.all()
    serializer_class = PeakSerializer

