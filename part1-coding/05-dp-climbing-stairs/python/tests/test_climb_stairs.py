from importlib.machinery import SourceFileLoader
import os
mod = SourceFileLoader('dp', os.path.join(os.path.dirname(__file__), '..', '05_dp_climbing_stairs.py')).load_module()

def test_climb():
    assert mod.climb_stairs(1) == 1
    assert mod.climb_stairs(2) == 2
    assert mod.climb_stairs(5) == 8
