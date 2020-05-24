"""
Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like following.
1) Count the number of expressions containing n pairs of parentheses which are correctly matched. For n = 3,
 possible expressions are ((())), ()(()), ()()(), (())(), (()()).


The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …

Using Binomial Coefficient
We can also use the below formula to find nth catalan number in O(n) time.
C(n)=(1/n+1)C{2n}{n}
"""
#Python program for nth Catalan Number 
# Returns value of Binomial Coefficient C(n, k) 
def binomialCoefficient(n, k): 

	# since C(n, k) = C(n, n - k) 
	if (k > n - k): 
		k = n - k 

	# initialize result 
	res = 1

	# Calculate value of [n * (n-1) *---* (n-k + 1)] 
	# / [k * (k-1) *----* 1] 
	for i in range(k): 
		res = res * (n - i) 
		res = res / (i + 1) 
	return res 

# A Binomial coefficient based function to 
# find nth catalan number in O(n) time 
def catalan(n): 
	c = binomialCoefficient(2*n, n) 
	return c/(n + 1) 

for i in range (10): 
    print (catalan(i),end=" ") 
