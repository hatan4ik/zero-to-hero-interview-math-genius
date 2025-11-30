from importlib.machinery import SourceFileLoader
import os
mod = SourceFileLoader('merge', os.path.join(os.path.dirname(__file__), '..', '04_intervals_merge.py')).load_module()

def test_merge_intervals():
    iv = [[1,3],[2,6],[8,10],[15,18]]
    assert mod.merge(iv) == [[1,6],[8,10],[15,18]]
