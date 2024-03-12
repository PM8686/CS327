from coverage_example import foo, bar, baz, Point, closest_pair

# We went through these simple examples in the slides, 
# but you can test them out here with the coverage tool

def test_foo():
    assert foo(1, 1) == 1
    assert foo(0, 0) == 0
    assert foo(1, 0) == 0

def test_baz():
    # assert baz(1, 1) == 3
    assert baz(1, 2) == 4
    assert baz(-1, -1) == -2

def test_closest_pair():
    # does not depend on Point.__eq__
    p_list = [Point(0,0), Point(3,5), Point(1,1)]
    assert closest_pair(p_list) == (p_list[0],  p_list[2])

    # relies on Point.__eq__ working properly
    p_list = [Point(0,0), Point(3,5), Point(1,1)]
    assert closest_pair(p_list) == (Point(0,0), Point(1,1))
