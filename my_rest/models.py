from django.db import models


class Articel(models.Model):
    name = models.CharField(max_length=100)
    auther = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} : {self.auther}"

