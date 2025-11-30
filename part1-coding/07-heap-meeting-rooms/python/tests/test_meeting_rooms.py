from importlib.machinery import SourceFileLoader
import os
mod = SourceFileLoader('heap', os.path.join(os.path.dirname(__file__), '..', '07_heap_meeting_rooms.py')).load_module()

def test_rooms():
    assert mod.min_meeting_rooms([[0,30],[5,10],[15,20]]) == 2
