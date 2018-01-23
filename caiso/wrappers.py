class GenerationMixDataWrapper:
    def __init__(self, data):
        self.data = data


    def generations(self):
        return list(map(GenerationDataWrapper, self.data))


class GenerationDataWrapper:
    def __init__(self, data):
        self.data = data


    def balancing_authority(self):
        return self.data['ba_name']


    def fuel(self):
        return self.data['fuel_name']


    def megawatts(self):
        return self.data['gen_MW']


    def market(self):
        return self.data['market']


    def timestamp(self):
        return self.data['timestamp']
