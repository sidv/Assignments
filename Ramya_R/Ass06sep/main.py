import sys

from calc import Calculator


if __name__ == '__main__':
    print('File executing')
    a, b = sys.argv[1], sys.argv[2]
    c = Calculator(int(a), int(b))
    print(c.sum())
    print(c.sub())
    print(c.mul())
    print(c.div())
    print(c.mod())
    print(c.power())	
	
	
	
	
	
	

