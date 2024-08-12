import sys

"""
    This calculates numerlogy values after pythogorean table for words which are passed as argument
    in other words using this 'table' can calculate numerology value for passwords  to gain lucky number combinations on sum which are 3, 4, 5, 6, 8 and 9
"""

a = ord('a')
A = ord('A')
z = ord('z')
Z = ord('Z')
l = ord('0')
L = ord('9')

alpha = ["1aAjJsS", "2bBkKtT", "3cClLuU", "4dDmMvV", "5eEnNwW", "6fFoOxX", "7gGpPyY", "8hHqQzZ", "9iIrR"]
num = []

def c09(c, a, b):
	if (ord(c) <= b and ord(c) >= a):
		return True
	else:
		return False

# ascii table nums
def ascii(a, b):
    for i in xrange(a, b + 1):
        print( str(i) )
        
# validate string
def valid(s):
	for c in s:
		if c09(c, l, L) != True and c09(c, a, z) != True and c09(c, A, Z) != True:
			return False
	return True

# finds number for char
def bycicle(c):
	for s in alpha:
		if c in s:
			num.append( int( s[0] ) )
			break

# print arr as one line
def print_line(arr):
	for a in arr:
		print( str(a) )
	print ("\n")

def print_res(arr):

	# print word with space in char
	print( " ".join( arr ) )

	# print numbers
	# print_line( num )

	# number sum
	print( str( sum( num ) ) )

# checks passed arg count
### main script part
if ( len( sys.argv ) == 2 ):

	if valid( sys.argv[1] ) == True:

		for c in sys.argv[1]:
			bycicle(c)

		print_res( sys.argv[1])
	else:
		print( 'String contains unknown symbols' )
	
else:
	print( "Pass only one arg!" )

