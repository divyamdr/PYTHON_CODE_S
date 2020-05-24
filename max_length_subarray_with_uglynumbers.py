# Python 3 implementation of the approach 

# Function to get the nth ugly number 
def uglyNumber(n): 
	
	# To store ugly numbers 
	ugly = [None for i in range(n)] 
	i2 = 0
	i3 = 0
	i5 = 0
	next_multiple_of_2 = 2
	next_multiple_of_3 = 3
	next_multiple_of_5 = 5
	next_ugly_no = 1

	ugly[0] = 1
	for i in range(1, n, 1): 
		next_ugly_no = min(next_multiple_of_2, 
					min(next_multiple_of_3, 
						next_multiple_of_5)) 
		ugly[i] = next_ugly_no 
		if (next_ugly_no == next_multiple_of_2): 
			i2 = i2 + 1
			next_multiple_of_2 = ugly[i2] * 2
		if (next_ugly_no == next_multiple_of_3): 
			i3 = i3 + 1
			next_multiple_of_3 = ugly[i3] * 3
		if (next_ugly_no == next_multiple_of_5): 
			i5 = i5 + 1
			next_multiple_of_5 = ugly[i5] * 5

	return next_ugly_no 

# Function to return the length of the 
# maximum sub-array of ugly numbers 
def maxUglySubarray(arr, n): 
	s = set() 
	i = 1

	# Insert ugly numbers in set 
	# which are less than 1000 
	while (1): 
		next_ugly_number = uglyNumber(i) 
		if (next_ugly_number >= 1000): 
			break
		s.add(next_ugly_number) 
		i += 1

	current_max = 0
	max_so_far = 0

	for i in range(n): 
		
		# Check if element is non ugly 
		if (arr[i] not in s): 
			current_max = 0

		# If element is ugly, than update 
		# current_max and max_so_far accordingly 
		else: 
			current_max += 1
			max_so_far = max(current_max, 
							max_so_far) 

	return max_so_far 

# Driver code 
if __name__ == '__main__': 
	arr = [1, 0, 6, 7, 320, 800, 100, 648] 
	n = len(arr) 
	print(maxUglySubarray(arr, n)) 
	
# This code is contributed by 
# Surendra_Gangwar 
