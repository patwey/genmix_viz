from django.http import HttpResponse
from django.shortcuts import render

from .models import BalancingAuthority, Fuel, GenerationMix, Generation

def index(request):
    balancing_authorities_count = BalancingAuthority.objects.count()
    fuels_count = Fuel.objects.count()
    generation_mixes_count = GenerationMix.objects.count()
    generations_count = Generation.objects.count()

    context = {
        'balancing_authorities_count': balancing_authorities_count,
        'fuels_count': fuels_count,
        'generation_mixes_count': generation_mixes_count,
        'generations_count': generations_count,
    }

    return render(request, 'caiso/index.html', context)
