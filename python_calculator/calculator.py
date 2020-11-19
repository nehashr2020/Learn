import pytest
import re


def sum(a,b):

    return float(a)+float(b)

def diff(a,b):
    if a>b:
        return float(a)-float(b)
    else:
        return float(b)-float(a)

def mult(a,b):

    return float(a)*float(b)


def check4no(givennumber):
    num_format = re.compile("(\d+(?:\.\d+)?)")
    isnumber = re.match(num_format,givennumber)
    
    if isnumber:
        return givennumber
    else:
        raise ValueError("Entered input is not a valid digit")

def ask_user():
    x = input("Enter first number:")
    check4no(x)

    y = input ("Enter second number:")
    check4no(y)
    return x,y


# --==Main==--

from optparse import OptionParser

parser = OptionParser()

parser.add_option('-o', type='choice', choices=['add', 'sub', 'mul', 'div'])

options, args = parser.parse_args()

print('Operation to be performed:', options.o)
    
if options.o == 'add':
    a,b = ask_user()
    print("RESULT: ",sum(a,b))
elif options.o == 'sub':
    a,b = ask_user()
    print("RESULT: ",diff(a,b))
elif options.o == 'mul':
    a,b = ask_user()
    print("RESULT: ", mult(a,b))
    
def test_sum_int():
	assert sum(3,2) == 5
	
def test_sum_float():
	assert sum(2.5,3.5) == 6
	
def test_check4no():

	with pytest.raises(ValueError,match="Entered input is not a valid digit"):
		check4no('a')

	




    

    
