# -*- coding:utf-8 -*-

# Import system
import time


class cached_static_ttl(object):

    def __init__(self, ttl):
        self.cache = {}
        self.ttl = ttl

    def __call__(self, func):
        def _memoized(*args, **kwargs):
            key = self._generate_key(func, args, kwargs)
            self.func = func
            now = time.time()
            try:

                value, last_update = self.cache[key]
                age = now - last_update
                if age > self.ttl:
                    raise AttributeError

                return value

            except (KeyError, AttributeError):
                value = self.func(*args, **kwargs)
                self.cache[key] = (value, now)
                return value

            except TypeError:
                return self.func(*args)
        return _memoized

    def _generate_key(self, func, args, kwargs):
        args_key = "__".join([str(arg) for arg in args[1:]])
        kwargs_key = "__".join(["%s:%s" % (key, kwargs[key]) for key in sorted(kwargs.keys())])
        key = "%s.%s:%s:%s" % (func.__module__, func.__name__, args_key, kwargs_key)
        return key
