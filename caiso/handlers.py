from .models import GenerationMix, BalancingAuthority, Fuel, Generation
from .adapters import GenerationAdapter


class GenerationMixDataHandler:
    def __init__(self, ba_name):
        self.ba_name = ba_name

    def store_latest(self):
        gen_mix_data = self.latest_gen_mix_data()
        gen_mix, created = GenerationMix.objects.get_or_create(timestamp=gen_mix_data.timestamp())
        self.store_generations(gen_mix_data.generations(), gen_mix)
        return gen_mix


    def latest_gen_mix_data(self):
        return GenerationAdapter.get_latest(self.ba_name)


    def store_generations(self, generation_data_set, gen_mix):
        for generation_data in generation_data_set:
            self.store_generation(generation_data, gen_mix)


    def store_generation(self, data, gen_mix):
        ba, created = BalancingAuthority.objects.get_or_create(name=data.balancing_authority())
        fuel, created = Fuel.objects.get_or_create(name=data.fuel())
        gen, created = Generation.objects.get_or_create(megawatts=data.megawatts(),
                                                        market=data.market(),
                                                        timestamp=data.timestamp(),
                                                        balancing_authority=ba,
                                                        fuel=fuel,
                                                        generation_mix=gen_mix)
        return gen
