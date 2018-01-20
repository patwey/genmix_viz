from django.contrib import admin

from .models import BalancingAuthority, Fuel, GenerationMix, Generation

admin.site.register(BalancingAuthority)
admin.site.register(Fuel)
admin.site.register(GenerationMix)
admin.site.register(Generation)
