# Android_patterns
All possible Android  patterns that we can create.A clear visualization using python and pygame library.
This is the simple visualization project of all possible android patterns.

Using pygame pytho module to view the graphics.

The rules to be followed to make any valid pattern:
1]A minimum of 4 contact points must be connected.
2]A maximum number is 9.
3]A contact point can only be used once.
4]An intermediate point between two connected points must be included in the pattern order,
unless it was previously used.
5]starting and ending point should be different
6]You cant lift the hand



1]using all combinations with the conditions
    ->start from the 4 points upto 9 points different valid combinations
    NOTE:During combination the order of the elements does matter.

    >>> from math import factorial as f

    >>> sum([f(9)/f(5),f(9)/f(4),f(9)/f(3),f(9)/f(2),f(9)/f(1),f(9)/f(0)])
    985824.0
    >>>

    #with atleast 4 points:
    So there are 9,85,824 different combinations.But all these are not valid.

    But the valid number of combinations is only 3,89,112.
