import calculator

class TestCalculator:

    def test_addition(self):
        assert 6==calculator.add(2,4)
    def test_subtraction(self):
        assert 2==calculator.sub(4,2)