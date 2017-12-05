from .models import Device, Tracking

from rest_framework import serializers


class TrackingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tracking
        fields = [
            'latitude',
            'longitude',
            'capture_time',
            'created_at',
            'updated_at',
        ]


class DeviceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            'id',
            'number',
            'network_operator',
            'active',
            'created_at',
            'updated_at'
        ]


# class DeviceDetailSerializer(serializers.ModelSerializer):
#     trackings = serializers.SerializerMethodField()
#
#     def get_trackings(self, obj):
#         trackings = Tracking.objects.filter(device__id=obj.id)
#         serializer = TrackingSerializer(context=trackings, many=True, )
#         return serializer.data
#
#     class Meta:
#         model = Device
#         fields = [
#             'trackings',
#             'number',
#             'network_operator',
#             'active',
#             'created_at',
#             'updated_at'
#         ]
