from django.shortcuts import render
from .models import Device, Tracking

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .serializers import DeviceListSerializer, TrackingSerializer


class TrackingListAPIView(ListAPIView):
    serializer_class = TrackingSerializer

    def get_queryset(self, *args, **kwargs):
        number = self.request.GET.get("number")
        device = Device.objects.get_object_or_none(number=number)

        if device is None:
            # return Response(data={"message": "device not found!"}, status=404)
            return None
        return Tracking.objects.filter(device=device)


class DeviceListAPIView(ListAPIView):
    serializer_class = DeviceListSerializer
    queryset = Device.objects.all()


class DeviceDetailAPIView(APIView):
    def get(self, *args, **kwargs):
        number = self.request.GET.get("number")
        device = Device.objects.get_object_or_none(number=number)

        if device is None:
            return Response(data={"message": "device not found!"}, status=404)
        trackings = Tracking.objects.filter(device=device)
        serializer = DeviceListSerializer(device)
        serializer2 = TrackingSerializer(trackings, many=True)
        response = {
            "device": serializer.data,
            "trackings": serializer2.data
        }
        return Response(data=response, status=200)
