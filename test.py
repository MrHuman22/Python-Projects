"""
Trying out the pytest module
"""
def add_one(a: int) -> int:
    return a + 1

def test_add_one():
    assert add_one(2) == 3