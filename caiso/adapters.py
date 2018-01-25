from pyiso import client_factory
from .wrappers import GenerationMixDataWrapper

class GenerationAdapter:
    def get_yesterday(ba_name):
        client = client_factory(ba_name)
        data = client.get_generation(yesterday=True)
        return GenerationMixDataWrapper(data)
