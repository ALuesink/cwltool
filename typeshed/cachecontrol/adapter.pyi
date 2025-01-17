# Stubs for cachecontrol.adapter (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from requests.adapters import HTTPAdapter

from .cache import DictCache as DictCache
from .controller import CacheController as CacheController
from .filewrapper import CallbackFileWrapper as CallbackFileWrapper

class CacheControlAdapter(HTTPAdapter):
    invalidating_methods = ...  # type: Any
    cache = ...  # type: Any
    heuristic = ...  # type: Any
    controller = ...  # type: Any
    def __init__(
        self,
        cache=None,
        cache_etags=True,
        controller_class=None,
        serializer=None,
        heuristic=None,
        *args,
        **kw
    ): ...
    def send(self, request, **kw): ...
    def build_response(self, request, response, from_cache=False): ...
    def close(self): ...
