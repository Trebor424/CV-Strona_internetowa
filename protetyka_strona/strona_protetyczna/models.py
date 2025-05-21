from django.db import models

class CennikPozycja(models.Model):
    nazwa = models.CharField(max_length=255)
    opis = models.TextField(blank=True, null=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nazwa

class OfertaPracy(models.Model):
    tytul = models.CharField(max_length=255)
    opis = models.TextField()
    data_dodania = models.DateTimeField(auto_now_add=True)
    aktywna = models.BooleanField(default=True)

    def __str__(self):
        return self.tytul