from importlib.machinery import SourceFileLoader
import os
mod = SourceFileLoader('topo', os.path.join(os.path.dirname(__file__), '..', '06_toposort_course_schedule.py')).load_module()

def test_topo_sort():
    n=4; edges=[(1,0),(2,0),(3,1),(3,2)]
    order = mod.topo_sort(n, edges)
    assert order is not None and set(order)==set(range(4))
