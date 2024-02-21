from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(4)) == 4*4
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(5)) == 5*5
    assert quadratic_multiply(BinaryNumber(6), BinaryNumber(6)) == 6*6
    assert quadratic_multiply(BinaryNumber(7), BinaryNumber(7)) == 7*7
    assert quadratic_multiply(BinaryNumber(8), BinaryNumber(8)) == 8*8
    assert quadratic_multiply(BinaryNumber(9), BinaryNumber(9)) == 9*9
    assert quadratic_multiply(BinaryNumber(10), BinaryNumber(10)) == 10*10
