from importlib.machinery import SourceFileLoader
import os
mod = SourceFileLoader('bfs', os.path.join(os.path.dirname(__file__), '..', '03_bfs_level_order.py')).load_module()

def test_level_order():
    # Build tree: 3 -> (9,20), 20 -> (15,7)
    n15 = mod.Node(15); n7 = mod.Node(7)
    n20 = mod.Node(20, n15, n7); n9 = mod.Node(9)
    root = mod.Node(3, n9, n20)
    assert mod.level_order(root) == [[3],[9,20],[15,7]]
