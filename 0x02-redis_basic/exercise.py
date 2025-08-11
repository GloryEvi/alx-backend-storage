#!/usr/bin/env python3
"""
Redis Cache module

This module provides a Cache class for storing and retrieving data
using Redis as the backend storage system.
"""
import redis
import uuid
from typing import Union, Optional, Callable


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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally apply a conversion function

        Args:
            key: The key to retrieve data for
            fn: Optional callable to convert the retrieved data

        Returns:
            The retrieved data, optionally converted by fn, or None if key
            doesn't exist
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data from Redis and convert to string

        Args:
            key: The key to retrieve data for

        Returns:
            The retrieved data as a UTF-8 decoded string, or None if key
            doesn't exist
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data from Redis and convert to integer

        Args:
            key: The key to retrieve data for

        Returns:
            The retrieved data as an integer, or None if key doesn't exist
        """
        return self.get(key, fn=int)
