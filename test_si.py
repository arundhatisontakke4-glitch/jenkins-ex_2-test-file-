from si import simple_interest

def test_simple_interest_1():
 assert simple_interest(1000, 5, 2) == 100

def test_simple_interest_2():
 assert simple_interest(2000, 10, 3) == 600