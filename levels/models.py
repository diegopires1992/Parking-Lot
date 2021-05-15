from django.db import models


class Avaliable(models.Model):
    available_motorcycle_spaces = models.IntegerField()
    available_car_spaces = models.IntegerField()

    def str(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=255)
    fill_priority = models.IntegerField()
    available_spaces = models.ForeignKey(Avaliable,on_delete=models.CASCADE, null=True)

    def str(self):
        return self.name