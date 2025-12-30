# Navigate to: /Users/vincent/Documents/Spigot/RaspberryJuicy/test/original/mcpi/util.py
# And replace the imports at the top of the file with this:

try:
    from collections.abc import Iterable
except ImportError:
    from collections import Iterable

# Then change line 5 from:
# if isinstance(e, collections.Iterable) and not isinstance(e, str):
# to:
# if isinstance(e, Iterable) and not isinstance(e, str):

# ===== COMPLETE FIXED VERSION OF util.py =====
import struct

try:
    from collections.abc import Iterable
except ImportError:
    from collections import Iterable

def flatten(l):
    for e in l:
        if isinstance(e, Iterable) and not isinstance(e, str):
            for ee in flatten(e):
                yield ee
        else:
            yield e

def _misc_to_bytes(m):
    return str(m).encode('utf-8')

def flatten_parameters_to_bytestring(l):
    return b",".join(map(_misc_to_bytes, flatten(l)))
