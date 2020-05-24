"""
Fuss–Catalan Numbers are a generalization of Catalan numbers that uses triplets instead of pairs.

The Fuss-Catalan Numbers can be represented by a Series with the formula:

The first few Fuss–Catalan Numbers are

1, 1, 3, 12, 55, 273, 1428, 7752, 43263, 246675………..

for n = 0, 1, 2, 3, … respectively

Applications of Fuss-Catalan number:

**** count no of squares in a polygon***

Count the number of ways to place parentheses among of 2n+1 numbers to be grouped three at a time.
Example: There are 3 ways to parenthesize {1, 2, 3, 4, 5} as triplets:
{{1, 2, 3}, 4, 5}, {1, {2, 3, 4}, 5}, {1, 2, {3, 4, 5}}

Count the number of complete ternary trees with n internal nodes.
"""


# Python3 program for nth Fuss–Catalan Number 

# Returns value of Binomial Coefficient C(n, k) 
def binomialCoeff(n, k) : 
    res = 1; 

	# Since C(n, k) = C(n, n-k) 
	if (k > n - k) : 
        k = n - k; 

	# Calculate value of 
	# [n*(n-1)*---*(n-k+1)] / [k*(k-1)*---*1] 
	for i in range(k) : 
		
		res *= (n - i); 
		res //= (i + 1); 

	return res; 

# A Binomial coefficient based function 
# to find nth Fuss–Catalan number in O(n) time 
def Fuss_catalan(n) : 

	# Calculate value of 3nCn 
	c = binomialCoeff(3 * n, n); 
	
	# return 3nCn/(2n+1) 
	return c // (2 * n + 1); 

# Driver code 
if __name__ == "__main__" : 

	for i in range(10) : 
		print(Fuss_catalan(i), end = " "); 
