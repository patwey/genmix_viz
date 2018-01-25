from .models import BalancingAuthority, Fuel, Generation
from .adapters import GenerationAdapter


class GenerationMixDataHandler:
    def __init__(self, ba_name):
        self.ba_name = ba_name

    def store_latest(self):
        gen_mix_data = self.yesterdays_gen_mix_data()
        for generation_data in gen_mix_data.generations():
            self.store_generation(generation_data)
        return gen_mix_data # TODO what do I want to return here?


    def yesterdays_gen_mix_data(self):
        return GenerationAdapter.get_yesterday(self.ba_name)


    def store_generation(self, data):
        ba, created = BalancingAuthority.objects.get_or_create(name=data.balancing_authority())
        fuel, created = Fuel.objects.get_or_create(name=data.fuel())
        gen, created = Generation.objects.get_or_create(
            megawatts=data.megawatts(),
            market=data.market(),
            timestamp=data.timestamp(),
            balancing_authority=ba,
            fuel=fuel,
        )
        return gen
