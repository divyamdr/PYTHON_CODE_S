"""
The Magic of Fibonacci Numbers
“Fibonacci Series”, sounds familiar, right?
An Easy To Understand sequence represented as 0 1 1 2 3 5 8 13…. where each number is the sum of the preceding two numbers, with the series starting from 0, 1. But, did you ever realise how magical these numbers are?
Let’s get deeper into these numbers in this article.
Fibonacci numbers appear in so many contexts in our lives and surroundings, for example, the number of the petals in a flower, the seed heads of a flower, paintings and a lot more. In fact, the beauty of a human face is based on Golden Ratio whose nth power forms the nth Fibonacci number. (nth Fibonacci number is 1.618n where 1.618 is the Golden ratio).
These numbers display a lot of magical patterns.
Given the Fibonacci numbers: 1 1 2 3 5 8 13 21 34 55 89…
Let’s square these numbers: 1 1 4 9 25 64 169…….
Let us now add more than 2 numbers of this squared series increasingly.
1+1+4 = 6
1+1+4+9 = 15
1+1+4+9+25 = 40
1+1+4+9+25+64 = 104
These do not seem to be Fibonacci numbers. But, if you analyse closely, you can see that these numbers enclose hidden Fibonacci numbers.
1+1+4=2* 3
1+1+4+9=3*5
1+1+4+9+25=5*8
1+1+4+9+25+64=8*13

Area of this rectangle = sum of the areas of squares inside it = 12+12+22+32+52+82
Also, Area of rectangle = length*breadth = 8*(8+5) = 104 which proves that
12+12+22+32+52+82 = 8 *13

If we continue this process of merging these squares to form rectangles, we can get rectangles with dimensions:
8*13
13*21
21*34
34*55
55*89….
If we divide the dimensions of these rectangles keeping the larger dimension in the numerator, we end up with these figures:
8*13 => 13/8= 1.625
13*21 => 21/13 =1.615
21*34 => 34/21 = 1.619
34*55 => 55/34 = 1.6176
55*89 =>89/55 = 1.61818

As we continue dividing the dimensions of larger rectangles, we would get close to 1.618033… which is defined as the Golden Ratio.
This Golden Ratio, particularly is of great interest to mathematicians since it holds great significance in our surroundings and environment.
"""