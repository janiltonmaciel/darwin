# -*- coding: utf-8 -*-
"""
    werkzeug.contrib.cache
    ~~~~~~~~~~~~~~~~~~~~~~

    The main problem with dynamic Web sites is, well, they're dynamic.  Each
    time a user requests a page, the webserver executes a lot of code, queries
    the database, renders templates until the visitor gets the page he sees.

    This is a lot more expensive than just loading a file from the file system
    and sending it to the visitor.

    For most Web applications, this overhead isn't a big deal but once it
    becomes, you will be glad to have a cache system in place.

    How Caching Works
    =================

    Caching is pretty simple.  Basically you have a cache object lurking around
    somewhere that is connected to a remote cache or the file system or
    something else.  When the request comes in you check if the current page
    is already in the cache and if so, you're returning it from the cache.
    Otherwise you generate the page and put it into the cache. (Or a fragment
    of the page, you don't have to cache the full thing)

    Here is a simple example of how to cache a sidebar for a template::

        def get_sidebar(user):
            identifier = 'sidebar_for/user%d' % user.id
            value = cache.get(identifier)
            if value is not None:
                return value
            value = generate_sidebar_for(user=user)
            cache.set(identifier, value, timeout=60 * 5)
            return value

    Creating a Cache Object
    =======================

    To create a cache object you just import the cache system of your choice
    from the cache module and instantiate it.  Then you can start working
    with that object:

    >>> from werkzeug.contrib.cache import SimpleCache
    >>> c = SimpleCache()
    >>> c.set("foo", "value")
    >>> c.get("foo")
    'value'
    >>> c.get("missing") is None
    True

    Please keep in mind that you have to create the cache and put it somewhere
    you have access to it (either as a module global you can import or you just
    put it into your WSGI application).

    :copyright: (c) 2011 by the Werkzeug Team, see AUTHORS for more details.
    :license: BSD, see LICENSE for more details.
"""


# Import system modules
from itertools import izip


def _items(mappingorseq):
    """Wrapper for efficient iteration over mappings represented by dicts
    or sequences::

        >>> for k, v in _items((i, i*i) for i in xrange(5)):
        ...    assert k*k == v

        >>> for k, v in _items(dict((i, i*i) for i in xrange(5))):
        ...    assert k*k == v

    """
    return mappingorseq.iteritems() if hasattr(mappingorseq, 'iteritems') \
        else mappingorseq


class BaseCache(object):
    """Baseclass for the cache systems.  All the cache systems implement this
    API or a superset of it.

    :param default_timeout: the default timeout that is used if no timeout is
                            specified on :meth:`set`.
    """

    def __init__(self, default_timeout=300, debug=False):
        self.default_timeout = default_timeout
        self.debug = debug

    def get(self, key):
        """Looks up key in the cache and returns the value for it.
        If the key does not exist `None` is returned instead.

        :param key: the key to be looked up.
        """
        return None

    def delete(self, key):
        """Deletes `key` from the cache.  If it does not exist in the cache
        nothing happens.

        :param key: the key to delete.
        """
        pass

    def get_many(self, *keys):
        """Returns a list of values for the given keys.
        For each key a item in the list is created.  Example::

            foo, bar = cache.get_many("foo", "bar")

        If a key can't be looked up `None` is returned for that key
        instead.

        :param keys: The function accepts multiple keys as positional
                     arguments.
        """
        return map(self.get, keys)

    def get_dict(self, *keys):
        """Works like :meth:`get_many` but returns a dict::

            d = cache.get_dict("foo", "bar")
            foo = d["foo"]
            bar = d["bar"]

        :param keys: The function accepts multiple keys as positional
                     arguments.
        """
        return dict(izip(keys, self.get_many(*keys)))

    def set(self, key, value, timeout=None):
        """Adds a new key/value to the cache (overwrites value, if key already
        exists in the cache).

        :param key: the key to set
        :param value: the value for the key
        :param timeout: the cache timeout for the key (if not specified,
                        it uses the default timeout).
        """
        pass

    def add(self, key, value, timeout=None):
        """Works like :meth:`set` but does not overwrite the values of already
        existing keys.

        :param key: the key to set
        :param value: the value for the key
        :param timeout: the cache timeout for the key or the default
                        timeout if not specified.
        """
        pass

    def set_many(self, mapping, timeout=None):
        """Sets multiple keys and values from a mapping.

        :param mapping: a mapping with the keys/values to set.
        :param timeout: the cache timeout for the key (if not specified,
                        it uses the default timeout).
        """
        for key, value in _items(mapping):
            self.set(key, value, timeout)

    def delete_many(self, *keys):
        """Deletes multiple keys at once.

        :param keys: The function accepts multiple keys as positional
                     arguments.
        """
        for key in keys:
            self.delete(key)

    def clear(self):
        """Clears the cache.  Keep in mind that not all caches support
        completely clearing the cache.
        """
        pass

    def inc(self, key, delta=1):
        """Increments the value of a key by `delta`.  If the key does
        not yet exist it is initialized with `delta`.

        For supporting caches this is an atomic operation.

        :param key: the key to increment.
        :param delta: the delta to add.
        """
        self.set(key, (self.get(key) or 0) + delta)

    def dec(self, key, delta=1):
        """Decrements the value of a key by `delta`.  If the key does
        not yet exist it is initialized with `-delta`.

        For supporting caches this is an atomic operation.

        :param key: the key to increment.
        :param delta: the delta to subtract.
        """
        self.set(key, (self.get(key) or 0) - delta)


class NullCache(BaseCache):
    """A cache that doesn't cache.  This can be useful for unit testing.

    :param default_timeout: a dummy parameter that is ignored but exists
                            for API compatibility with other caches.
    """





