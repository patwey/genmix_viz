from .models import BalancingAuthority, GenerationMix, Fuel, Generation
from .adapters import GenerationAdapter


class GenerationMixHandler:
    def __init__(self, ba_name):
        self.ba_name = ba_name
        self.gms = {}
        self.bas = {}
        self.fs = {}


    def store_yesterday(self):
        gms_data = self.yesterdays_mix_data()

        for g in gms_data.generations():
            ba = self.get_or_create_balancing_authority(g.balancing_authority())
            gm = self.get_or_create_generation_mix(g.timestamp(), ba)
            f = self.get_or_create_fuel(g.fuel())
            self.get_or_create_generation(g.megawatts(), g.market(), f, gm)

        return gms_data


    def yesterdays_mix_data(self):
        return GenerationAdapter.get_yesterday(self.ba_name)


    def get_or_create_balancing_authority(self, name):
        if name in self.bas:
            ba = self.bas[name]
        else:
            ba = BalancingAuthority.objects.get_or_create(name=name)[0]
            self.bas[ba.name] = ba

        return ba


    def get_or_create_generation_mix(self, timestamp, ba):
        if timestamp in self.gms:
            gm = self.gms[timestamp]
        else:
            gm = GenerationMix.objects.get_or_create(timestamp=timestamp,
                                                     balancing_authority=ba)[0]
            self.gms[gm.timestamp] = gm

        return gm


    def get_or_create_fuel(self, name):
        if name in self.fs:
            f = self.fs[name]
        else:
            f = Fuel.objects.get_or_create(name=name)[0]
            self.fs[f.name] = f

        return f


    def get_or_create_generation(self, megawatts, market, f, gm):
        return Generation.objects.get_or_create(megawatts=megawatts,
                                                market=market,
                                                fuel=f,
                                                generation_mix=gm)
