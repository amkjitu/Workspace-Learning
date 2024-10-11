# PokerTest

This project was based off of a Simulation Models assignment I was given. I developed an algorithm for finding out the category that a random number's characters would fall in to.

# Problem

Another test for independence is called the poker test, in which the occurrence of patterns of digits in the sample is compared with the known probabilities of these patterns occurring in theory, with the patterns being those possible in a poker hand.  More specifically, the following probabilities for patterns in five-digit numbers are known:

| Pattern                     | Probability                                |
|-----------------------------|--------------------------------------------|
| Five different              | .9\*.8\*.7\*.6 = .3024                        |
| Exactly one pair            | (5\!)/(2\!\*3\!)\*.9\*.8\*.7\*.1 = .5040           |
| Exactly two pairs           | \[(5\!)/(4\!)\]\*\[(3\!/(2\!)\]\*.1\*.1\*.9\*.8 = .1080 |
| Exactly three of a kind     | \[(5\!)/\[(3\!)\*(2\!)\]\*.9\*.8\*.1\*.1 = .0720      |
| Three of kind plus one pair | \[(5\!)/\[(3\!)\*(2\!)\]\*.9\*.1\*.1\*.1 = .0090      |
| Four of a kind              | \[(5\!)/(4\!)\]\*.9\*.1\*.1\*.1 = .0045            |
| Five of a kind              | .1\*.1\*.1\*.1 = .0001                        |


Multiplying by the sample size n provides the expected number of occurrences of each pattern.  For this task, you are to process the set of 800 random numbers in the table, for each one determining which of the 7 patterns they fit in the poker hand.

# Solution

I decided that a hashmap would be a reasonable data structure to use here. I came to this conclusion simply because the classifications were based upon the number of repetitions of a digit in a random number, as opposed to say a run in a "poker hand".

After choosing a hashmap the problem came easily. I simply had to split each number into a char array, add them to the hashmap if they didn't exist already and assign a 1 as their value, or increment the value by one if the key did exist.

Finally, my approach lent to easy classification, each type of possible output of the hashmap was easily testable in a big if statement, and thus classification only took a few lines.
