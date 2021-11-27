from django.db import models

class soz(models.Model):
    id = models.IntegerField(primary_key=True)
    correct = models.CharField(max_length=20)
    def __str__(self):
        return self.correct

class nosoz(models.Model):
    wrong = models.CharField(max_length=20)
    soz_id = models.ForeignKey(soz, on_delete=models.CASCADE)
    def __str__(self):
        return self.wrong
