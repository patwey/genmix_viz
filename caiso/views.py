from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from .models import BalancingAuthority
from .serializers import GenerationSerializer


@csrf_exempt
def latest_generation_day(request):
    gens = []

    try:
        ba = BalancingAuthority.objects.get(name='CAISO') # TODO hard-coded
        # gens = ba.generation_set.filter(timestamp__contains=date.today()) # TODO: filter by today's date
        gens = ba.generation_set.all()
    except: # TODO handle specific exceptions?
        return HttpResponse(status=404)

    serializer = GenerationSerializer(gens, many=True)
    data = dict(generations=serializer.data)

    return JsonResponse(data)
