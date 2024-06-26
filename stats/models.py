from django.db import models
from main.models import *
from user.models import *


class Sotuv(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdor = models.FloatField()
    summa = models.FloatField()
    tolandi = models.FloatField(default=0)
    qarz = models.FloatField(default=0)
    sana = models.DateField()
    tarqatuvchi = models.ForeignKey(Tarqatuvchi, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.mahsulot.nom} {self.mijoz.ism}"
