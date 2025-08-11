# Redis Basic Operations

A Python implementation of basic Redis operations with caching, method call tracking, and history management functionality.

## Description

This project implements a Cache class that provides an interface to store and retrieve data from Redis using automatically generated keys. The implementation includes decorators for tracking method calls and maintaining call history, along with utility functions for data analysis.

## Features

- **Data Storage**: Store strings, bytes, integers, and floats with auto-generated UUID keys
- **Data Retrieval**: Retrieve data with optional type conversion functions
- **Call Counting**: Track the number of times methods are called using Redis counters
- **Call History**: Maintain complete history of method inputs and outputs
- **History Replay**: Display formatted call history for analysis and debugging
- **Type Conversion**: Built-in methods for string and integer conversion

## Requirements

- Ubuntu 18.04 LTS
- Python 3.7
- Redis server
- Redis Python client
- pycodestyle (version 2.5) for code formatting

## Installation

### Install Redis Server
```bash
sudo apt-get update
sudo apt-get -y install redis-server
sudo apt install python3-redis
```

### Configure Redis
```bash
sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
sudo service redis-server start
```

### Verify Installation
```bash
redis-cli ping  # Should return PONG
python3 -c "import redis; r = redis.Redis(); print(r.ping())"  # Should return True
```

## Usage

### Basic Cache Operations

```python
from exercise import Cache

# Initialize cache
cache = Cache()

# Store data (returns UUID key)
key1 = cache.store("Hello World")
key2 = cache.store(42)
key3 = cache.store(b"binary data")

# Retrieve data
data = cache.get(key1)  # Returns b"Hello World"
text = cache.get_str(key1)  # Returns "Hello World"
number = cache.get_int(key2)  # Returns 42
```

### Method Call Tracking

```python
from exercise import Cache

cache = Cache()

# Each store call is automatically tracked
cache.store("first")
cache.store("second") 
cache.store("third")

# Check call count
count = cache.get(cache.store.__qualname__)
print(f"Store method called {count.decode()} times")
```

### Call History Analysis

```python
from exercise import Cache, replay

cache = Cache()

# Make some calls
cache.store("foo")
cache.store("bar")
cache.store(42)

# Display call history
replay(cache.store)
```

Output:
```
Cache.store was called 3 times:
Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f
Cache.store(*('bar',)) -> dcddd00c-4219-4dd7-8877-66afbe8e7df8
Cache.store(*(42,)) -> 5e752f2b-ecd8-4925-a3ce-e2efdee08d20
```

## API Reference

### Cache Class

#### `__init__()`
Initializes the Cache instance with a clean Redis database.

#### `store(data: Union[str, bytes, int, float]) -> str`
Stores data in Redis with an auto-generated UUID key.
- **Parameters**: `data` - The data to store
- **Returns**: String UUID key for the stored data

#### `get(key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]`
Retrieves data from Redis with optional conversion function.
- **Parameters**: 
  - `key` - The key to retrieve data for
  - `fn` - Optional callable to convert the retrieved data
- **Returns**: Retrieved data (optionally converted) or None

#### `get_str(key: str) -> Optional[str]`
Retrieves data and converts to UTF-8 string.
- **Parameters**: `key` - The key to retrieve data for
- **Returns**: String data or None

#### `get_int(key: str) -> Optional[int]`
Retrieves data and converts to integer.
- **Parameters**: `key` - The key to retrieve data for
- **Returns**: Integer data or None

### Decorators

#### `@count_calls`
Tracks the number of times a decorated method is called using Redis INCR.

#### `@call_history`
Stores the complete history of inputs and outputs for a decorated method using Redis lists.

### Utility Functions

#### `replay(method: Callable) -> None`
Displays formatted call history for a given method.
- **Parameters**: `method` - The method to display history for

## File Structure

```
0x02-redis_basic/
├── exercise.py          # Main implementation file
├── main.py             # Basic functionality tests
├── main_task2.py       # Call counting tests
├── main_task3.py       # Call history tests  
├── main_task4.py       # Replay function tests
├── test_cache.py       # Comprehensive test suite
└── README.md           # This file
```

## Code Quality

This project follows:
- PEP 8 style guidelines enforced by pycodestyle
- Comprehensive docstrings for all modules, classes, and methods
- Type annotations for all functions and methods
- Proper error handling and edge case management

## Testing

Run individual test files to verify functionality:

```bash
python3 main.py              # Basic operations
python3 main_task2.py        # Call counting
python3 main_task3.py        # Call history
python3 main_task4.py        # Replay function
python3 test_cache.py        # Comprehensive tests
```

Verify code quality:
```bash
python3 -m pycodestyle exercise.py
```

## Redis Commands Used

- `SET` / `GET` - Basic key-value operations
- `INCR` - Atomic counter incrementing
- `RPUSH` - Append to lists (right push)
- `LRANGE` - Retrieve list ranges
- `FLUSHDB` - Clear database

## Contributing

When contributing to this project:

1. Ensure all functions have proper type annotations
2. Include comprehensive docstrings
3. Follow pycodestyle guidelines
4. Add tests for new functionality
5. Update documentation as needed

## License

This project is part of the ALX Backend Storage curriculum.