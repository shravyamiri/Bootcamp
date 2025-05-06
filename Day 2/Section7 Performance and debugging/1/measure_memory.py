
from memory_profiler import profile

@profile
def use_memory():
    a = [x for x in range(1000000)]
    return sum(a)

use_memory()