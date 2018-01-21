from pyiso import client_factory
from .wrappers import GenerationMixDataWrapper

class GenerationAdapter:
    def get_latest(balancing_authority_name):
        client = client_factory(balancing_authority_name)
        data = client.get_generation(latest=True)
        return GenerationMixDataWrapper(data)
