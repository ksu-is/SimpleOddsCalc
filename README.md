SimpleOddsCalc
======================

Program to teach how to do simple odds for Texas Hold-em.

I would like to write a program that trains people how to calculate the simple equity of a Texas holdem hand with a given board. With 2 people on this project, I think some more advanced calculations may be done, but I think I may be able to write this program for simple equity on my own. Equity in a poker hand is the percentage that you are likely to win a hand. There are complex calculators on the web currently that can give a person a very close approximation, but my program would help poker players learn how to do a quick calculation in their head. There would be two parts of the program, one would be for users to see two hole-cards and a board and input the simple equity into the program to see if they are right or wrong, and a second part where a user can enter two hole-cards and a board to see what the equity calculation would be. The first function of the program would be to test a user’s ability to calculate their simple equity. Users would be able to set how long they are given to calculate the percentage. Then, the user would be able to see the hand they are given and what cards are on the board. Once the user enters their guess for the percentage the program would tell them if they were right or wrong and display the correct percentage. The second function of the program would be to let the user input a two-card hand and enter the cards on the board (a 3 card “flop”, or the “flop” and the 1 “turn” card). This would be helpful to the user as they are able to check specific combinations instead of the randomly generated scenarios from the first function of the program. https://github.com/ksu-is/texas-holdem - I can reference this project for some of the logic and input from the user. https://github.com/ktseng/holdem_calc - This program goes a bit further with more complex calculations of odds, but may be useful and I can reference this program for harder but more accurate calculations.

As the project is completed, a write up of how the program functions will be put here.

Background
-----------------
Equity is an important concept in Texas Holdem. It is the percentage of times you will win a hand with a given hand and board state. This is one of many concepts that the best players use at the table to make decisions.

While a Monte Carlo simulation is significantly better in telling us what the odds are and the equity of any given hand, doing 100,000 simulations in our head at the table is not feasible. We can, however, approximate the odds using a few methods.

The "Seen Cards" Method
-----------------
One of the better ways to do quick math at the table is to determine your outs, and divide that by the remaining cards in the deck. For example, if you see your two cards and the 3 card flop, you would divide your outs by the remaining 47 cards.

There are some limitations, though. What if your opponent(s) have one of your outs? What if someone folded one of your outs? What if one of your outs improves your hand but gives your opponent a better hand?

This program is not meant to factor in every single situation at the table. Because those decisions are entirely subjective, this program focuses on the math. Use this program as a way to learn how to do the math at the table quickly.

The "4 and 2" Method
-----------------
- If time allows, this may be added

User Entry for Odds
-----------------

Examples of Input and Output
-----------------