from rest_framework import serializers

class AvaliableSerializers(serializers.Serializer):
    available_motorcycle_spaces = serializers.IntegerField()
    available_car_spaces = serializers.IntegerField()

class LevelSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    fill_priority = serializers.IntegerField()
    available_spaces = AvaliableSerializers(read_only=True)
