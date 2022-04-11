from django.db import models

class Pokemon(models.Model):
    serial = models.IntegerField(null = True)
    name = models.CharField(max_length=50)
    type1 = models.CharField(max_length=50)
    type2 = models.CharField(max_length=50, null = True)
    generation = models.IntegerField(null = True)

    def __str__(self):
        return self.name
