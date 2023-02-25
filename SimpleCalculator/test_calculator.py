import unittest
from calculator import Calculator

# Fenix Kanat
class test_calculator(unittest.TestCase):

    def test_add(self):
        
        self.assertEqual(Calculator.add(3,4),7)
        self.assertEqual(Calculator.add(1,1),2)
        self.assertEqual(Calculator.add(0,0),0)
        self.assertEqual(Calculator.add(-1,-1),-2)
        self.assertEqual(Calculator.add(-1,1),0)
        self.assertEqual(Calculator.add(150,150),300)
        

    def test_multiply(self):

        self.assertEqual(Calculator.multiply(2,3),6)
        self.assertEqual(Calculator.multiply (5,5),25)
        self.assertEqual(Calculator.multiply (0,0),0)
        self.assertEqual(Calculator.multiply (-1,-1),1)
        self.assertEqual(Calculator.multiply (-1,1),-1)
        self.assertEqual(Calculator.multiply (10,10),100)

    def test_subtract(self):

        self.assertEqual(Calculator.subtract(5,5),0)
        self.assertEqual(Calculator.subtract(0,0),0)
        self.assertEqual(Calculator.subtract(-1,-1),0)
        self.assertEqual(Calculator.subtract(-1,1),-2)
        self.assertEqual(Calculator.subtract(100,50),50)
        self.assertEqual(Calculator.subtract(50,100),-50)



    def test_divide(self):

        self.assertEqual(Calculator.divide(4,2),2)
        self.assertEqual(Calculator.divide(1,1),1)
        self.assertEqual(Calculator.divide(-1,1),-1)
        self.assertEqual(Calculator.divide(50,25),2)

        with self.assertRaises(ZeroDivisionError):
            Calculator.divide(50,0)


if __name__ == '__main__':
    unittest.main()