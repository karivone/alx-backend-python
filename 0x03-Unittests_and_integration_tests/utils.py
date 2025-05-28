#!/usr/bin/env python3
"""Utility functions for nested map access, JSON requests, and memoization."""

import requests


def access_nested_map(nested_map, path):
    """Access a nested map with a given path tuple."""
    for key in path:
        nested_map = nested_map[key]
    return nested_map


def get_json(url):
    """Make a GET request and return the JSON payload."""
    response = requests.get(url)
    return response.json()


def memoize(method):
    """Memoize a method (usually a property) so it's only computed once."""
    attr_name = "_{}".format(method.__name__)

    @property
    def memoized(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, method(self))
        return getattr(self, attr_name)

    return memoized
