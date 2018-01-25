from pyiso import client_factory
from .wrappers import GenerationMixDataWrapper

class GenerationAdapter:
    def get_yesterday(balancing_authority_name):
        client = client_factory(balancing_authority_name)
        data = client.get_generation(yesterday=True)
        return GenerationMixDataWrapper(data)
