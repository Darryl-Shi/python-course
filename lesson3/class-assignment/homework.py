'''
#### Alien Points
- Make a list of ten aliens, each of which is one color: 'red', 'green', or 'blue'.
    - You can shorten this to 'r', 'g', and 'b' if you want, but if you choose this option you have to include a comment explaining what r, g, and b stand for.
- Red aliens are worth 5 points, green aliens are worth 10 points, and blue aliens are worth 20 points.
- Use a for loop to determine the number of points a player would earn for destroying all of the aliens in your list.

#### Gaussian Addition
This challenge is inspired by a story about the mathematician Carl Frederich Gauss. As the story goes, when young Gauss was in grade school his teacher got mad at his class one day.

"I'll keep the lot of you busy for a while", the teacher said sternly to the group. "You are to add the numbers from 1 to 100, and you are not to say a word until you are done."

The teacher expected a good period of quiet time, but a moment later our mathematician-to-be raised his hand with the answer. "It's 5050!" Gauss had realized that if you list all the numbers from 1 to 100, you can always match the first and last numbers in the list and get a common answer:

    1, 2, 3, ..., 98, 99, 100
    1 + 100 = 101
    2 + 99 = 101
    3 + 98 = 101

Gauss realized there were exactly 50 pairs of numbers in the range 1 to 100, so he did a quick calculation: 50 * 101 = 5050.

- Write a program that adds up a list of numbers.
    - The program should use a while loop to keep popping the first and last numbers from the list and calculate the sum of those two numbers.
    - The program should print out the current numbers that are being added, and print their partial sum.
    - The program should keep track of how many partial sums there are.
    - The program should then print out how many partial sums there were.
    - The program should perform Gauss' multiplication, and report the final answer.
- Prove that your program works, by passing in the range 1-100, and verifying that you get 5050.
    - `list(range(1,101))`
'''