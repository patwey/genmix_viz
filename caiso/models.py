from django.db import models


class BalancingAuthority(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class GenerationMix(models.Model):
    timestamp = models.DateTimeField()
    balancing_authority = models.ForeignKey(BalancingAuthority, on_delete=models.CASCADE)


    def __str__(self):
        return '%s' % self.timestamp


class Fuel(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Generation(models.Model):
    megawatts = models.FloatField()
    market = models.CharField(max_length=200)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    generation_mix = models.ForeignKey(GenerationMix, on_delete=models.CASCADE)


    def __str__(self):
        return '%s' % self.megawatts
