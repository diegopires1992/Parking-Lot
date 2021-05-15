from rest_framework import serializers

class SpaceSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    variety = serializers.CharField()
    level_name = serializers.CharField()

class VehiclesSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    license_plate = serializers.CharField()
    vehicle_type = serializers.CharField()
    arrived_at = serializers.DateTimeField(read_only=True)
    paid_at = serializers.DateTimeField(read_only=True)
    amount_paid = serializers.CharField(read_only=True)
    space = SpaceSerializers(read_only=True)
