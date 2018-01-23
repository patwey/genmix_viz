from django.db import models
from pytz import timezone


class BalancingAuthority(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Fuel(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Generation(models.Model):
    timestamp = models.DateTimeField()
    megawatts = models.FloatField()
    market = models.CharField(max_length=200)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    balancing_authority = models.ForeignKey(BalancingAuthority, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.timestamp.astimezone(timezone('America/Los_Angeles')).strftime("%B %d, %Y: %I:%M %p") # TODO how do I want this formatted?
