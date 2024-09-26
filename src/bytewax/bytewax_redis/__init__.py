"""A Bytewax connector for Redis."""

import os
import sys

from .sinks import RedisKVSink, RedisStreamSink
from .sources import RedisStreamSource

__all__ = ["RedisKVSink", "RedisStreamSink", "RedisStreamSource"]

if "BYTEWAX_LICENSE" not in os.environ:
    msg = (
        "`bytewax-redis` is commercially licensed "
        "with publicly available source code.\n"
        "You are welcome to prototype using this module for free, "
        "but any use on business data requires a paid license.\n"
        "See https://modules.bytewax.io/ for a license. "
        "Set the env var `BYTEWAX_LICENSE=1` to suppress this message."
    )
    print(msg, file=sys.stderr)
