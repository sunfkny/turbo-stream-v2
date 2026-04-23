# turbo-stream-v2

A Python library for decoding React Router's Turbo Stream v2 serialized data. The core logic is directly copied from [react-router](https://github.com/remix-run/react-router/blob/main/packages/react-router/vendor/turbo-stream-v2/).

## Installation

```bash
uv add git+https://github.com/sunfkny/turbo-stream-v2
```

## Usage

```python
import turbo_stream_v2

# Decode serialized Turbo Stream data
result = turbo_stream_v2.decode(data_bytes)

# result is a Python dict/object
print(result)
```

The `decode()` function accepts bytes input containing the serialized Turbo Stream format and returns a parsed Python dictionary.

## Requirements

- Python 3.13+
- Node.js 22.18+ (bundled via nodejs-wheel-binaries)

## How It Works

This library wraps the TypeScript implementation from React Router. When you call `decode()`, it:

1. Passes the serialized data to a Node.js subprocess running the TypeScript decoder
2. The decoder parses the line-based Turbo Stream format, handling:
   - Flattened JSON objects with reference IDs
   - Deferred values (promises that resolve later)
   - Error propagation
3. Returns the fully reconstructed Python object
