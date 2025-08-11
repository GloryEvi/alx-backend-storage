#!/usr/bin/env python3
"""
Redis Cache module

This module provides a Cache class for storing and retrieving data
using Redis as the backend storage system.
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class for Redis operations
    This class provides an interface to store and retrieve data from Redis
    using automatically generated keys for data storage.
    """

    def __init__(self) -> None:
        """
        Initialize the Cache instance

        Creates a Redis client instance and flushes the database
        to start with a clean state.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key

        Args:
            data: The data to store. Can be a string, bytes, integer, or float.

        Returns:
            str: The randomly generated key used to store the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    