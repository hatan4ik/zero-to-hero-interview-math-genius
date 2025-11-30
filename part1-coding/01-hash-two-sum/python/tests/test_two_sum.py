import importlib, os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
mod = importlib.import_module('01_hash_two_sum') if False else None
# Fallback: dynamic import by path
from importlib.machinery import SourceFileLoader
two = SourceFileLoader('two', os.path.join(os.path.dirname(__file__), '..', '01_hash_two_sum.py')).load_module()

def test_two_sum_basic():
    assert two.two_sum([2,7,11,15], 9) == [0,1]
    r = two.two_sum([3,2,4], 6)
    assert sorted(r) == [1,2]
