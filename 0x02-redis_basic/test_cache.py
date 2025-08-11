#!/usr/bin/env python3
"""
Test file for Cache class
"""
from exercise import Cache

cache = Cache()

# Test the provided test cases
TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    result = cache.get(key, fn=fn)
    assert result == value
    print(f"✓ Stored {value}, retrieved {result}")

# Test get_str method
key_str = cache.store("hello world")
retrieved_str = cache.get_str(key_str)
print(f"✓ get_str: {retrieved_str}")

# Test get_int method
key_int = cache.store(42)
retrieved_int = cache.get_int(key_int)
print(f"✓ get_int: {retrieved_int}")

print("All tests passed!")