from datetime import datetime


class GenerationMixSerializer:
    def __init__(self, generation_mix):
        self.generation_mix = generation_mix


    def data(self):
        result = {}
        result['timestamp'] = self.timestamp()

        for generation in self.generation_mix.generation_set.all():
            result[generation.fuel.name] = generation.megawatts

        return result


    def timestamp(self):
        timestamp = self.generation_mix.timestamp
        return (timestamp - self.epoch(timestamp.tzinfo)).total_seconds()


    def epoch(self, tzinfo):
        return datetime(1970, 1, 1, tzinfo=tzinfo)
