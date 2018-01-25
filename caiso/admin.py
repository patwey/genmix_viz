from django.contrib import admin

from .models import BalancingAuthority, Fuel, Generation, GenerationMix

admin.site.register(BalancingAuthority)
admin.site.register(Fuel)
admin.site.register(Generation)
admin.site.register(GenerationMix)
