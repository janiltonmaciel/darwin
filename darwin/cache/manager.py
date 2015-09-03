# -*- coding:utf-8 -*-

# import system
from tornado.options import options

# import local
from darwin.cache.client import NullCache
from darwin.cache.client.simple import SimpleCache
from darwin.cache.client.redis import RedisCache


cache_static = SimpleCache()
cache = None


def config_cache(client_type, params):
    global cache

    if client_type == "redis":
        cache = RedisCache(**params)
    elif client_type == "dummy":
        cache = NullCache()


#
# def reload_connection():
#     if options.cache_backend == "redis":
#         from bookcare.api.core.cache.cache_client import RedisCache
#
#         parametros = {
#             "host": options.cache_host,
#             "port": options.cache_port,
#             "password": options.cache_password,
#             "default_timeout": options.cache_timeout,
#         }
#         return RedisCache(**parametros)
#
#     elif options.cache_backend == "dummy":
#         from bookcare.api.core.cache.cache_client import NullCache
#         return NullCache()
#
#     return None
