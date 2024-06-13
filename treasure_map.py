"""This is a difficult challenge. 💪

You are going to write a program that will mark a spot on a map with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what it looks like, notice the nesting:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{line1}\n{line2}\n{line3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

 1 ['⬜️', '⬜️', '⬜️']

 2 ['⬜️', '⬜️', '⬜️']

3 ['⬜️', '⬜️', '⬜️']
Now it looks a bit more like the coordinates of a real map:


Your job is to write a program that allows you to mark a square on the map using a letter-number system.


So an input of A3 should place an X at the position shown below:


First, your program must take the user input and convert it to a usable format.

Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
Example Input 1
B3
Example Output 1
Hiding your treasure! X marks the spot.
['⬜️', '️⬜️', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', 'X', '⬜️️']
Example Input 2
B1
Example Output 2
Hiding your treasure! X marks the spot.
['⬜️', 'X', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', '⬜️️', '⬜️️']
Hints
See if this List method helps you: https://www.w3schools.com/python/ref_list_index.asp

Remember that nested Lists in Python are accessed from outside to inside. e.g. In the List below:

list = [['A', 'B, 'C'], 'E', 'F', 'G']
E is list[1] C is list[0][2]

Check your formatting. This is correctly formatted:
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']
vs.

Incorrectly formatted (missing a space before 'X and extra space after the X and extra space before the comma):

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️','X ' , '⬜️']"""

# First, your program must take the user input and convert it to a usable format.
# Next, you need to use that input to update your nested list with an "X".

# Your job is to write a program that allows you to mark a square on the map using a letter-number system.


"""
1A 1B 1C   [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
2A 2B 2C       0 [0, 1, 2]  ,   1 [0, 1, 2]   ,      2 [0, 1, 2]
3A 3B 3C



"""

line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map_value = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")

position = input("Write here the position: ")

# B2 - 2B
position_1 = position[0]
position_2 = position[1]

position_1, position_2 = position_2, position_1

if position_1 == "1":
    position_0 = line1
elif position_1 == "2":
    position_0 = line2
else:
    position_0 = line3

if position_2 == "A":
    position_0[0] = "X"
elif position_2 == "B":
    position_0[1] = "X"
else:
    position_0[2] = "X"

#print(f"{line1}\n{line2}\n{line3}")

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map_value = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")

position = input("Write here the position: ")

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map_value[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")
