from importlib.machinery import SourceFileLoader
import os
mod = SourceFileLoader('win', os.path.join(os.path.dirname(__file__), '..', '02_sliding_window_longest_substring.py')).load_module()

def test_longest():
    assert mod.longest_unique("abba") == 2
    assert mod.longest_unique("abcabcbb") == 3
