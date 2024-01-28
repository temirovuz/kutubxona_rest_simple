from django.db import models


class Kitob(models.Model):
    nomi = models.CharField(max_length=255)
    kitob_haqida = models.TextField()
    muallif = models.CharField(max_length=200)
    janr = models.CharField(max_length=200)
    isbn = models.IntegerField()
    narxi = models.IntegerField()


    def __str__(self):
        return self.nomi
