from rest_framework import serializers

class AvaliableSerializers(serializers.Serializer):
    avaliable_motorcycle_spaces = serializers.IntegerField()
    avaliable_car_spaces = serializers.IntegerField()

class LevelSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    fill_priority = serializers.IntegerField()
    avaliable_spaces = AvaliableSerializers(read_only=True)
