import calculator

class TestCalculator:

    def test_addition(self):
        assert 6==calculator.add(2,4)
        
    def test_subtraction(self):
        assert 2==calculator.sub(4,2)

    def test_multiplication(self):
        assert 100==calculator.multiply(10,10)

