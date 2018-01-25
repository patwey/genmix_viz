from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import BalancingAuthority, GenerationMix
from .serializers import GenerationMixSerializer


def index(request):
    return render(request, 'caiso/index.html')


@csrf_exempt
def yesterdays_mixes(request):
    ba = BalancingAuthority.objects.get(name='CAISO')
    gms = GenerationMix.objects.filter(balancing_authority=ba)[:24]
    gms = sorted(gms, key=lambda gm: gm.timestamp)

    serialized_gms = []
    for gm in gms:
        serialized_gms.append(GenerationMixSerializer(gm).data())

    return JsonResponse({ 'generation_mixes': serialized_gms })
