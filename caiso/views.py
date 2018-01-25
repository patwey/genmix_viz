from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import BalancingAuthority, Generation
from .serializers import GenerationSerializer


def index(request):
    return render(request, 'caiso/index.html')


@csrf_exempt
def latest_generation_day(request):
    gens = list(Generation.objects.all())
    gen_mixes = format_data(gens)
    return JsonResponse({ 'generation_mixes': gen_mixes })


from pytz import timezone
def to_pst(ts):
    return ts.astimezone(timezone('America/Los_Angeles'))


def format_data(gens):
    result = {}

    for gen in gens:
        pst_time = to_epoch_time(to_pst(gen.timestamp))
        if pst_time not in result:
            result[pst_time] = { 'time': pst_time }

        result[pst_time][gen.fuel.name] = gen.megawatts

    return list(result.values())


def to_epoch_time(ts):
    tz = ts.tzinfo
    return (ts-datetime(1970,1,1, tzinfo=tz)).total_seconds()
