#CONDITIONS (15PTS TOTAL)
import math
# PROBLEM 1 (GPA - 4pts)
# Grades are values between 0 and 100
# We will translate grades to letters using:
# http://www.collegeboard.com/html/academicTracker-howtoconvert.html
# Make a variable for your percentage grade.
# Make a series of if/elif/else statements to print the letter grade.
# If the user enters a grade lower than zero or higher than 100, just give an error message.
# Don't worry about making an exception for these right now.


percentage = 96
if percentage >= 97 and percentage <= 100:
    letter_grade = "A+"
elif percentage < 97 and percentage >= 93:
    letter_grade = "A"
elif percentage < 93 and percentage >= 90:
    letter_grade = "A-"
elif percentage < 90 and percentage >= 87:
    letter_grade = "B+"
elif percentage < 87 and percentage >= 83:
    letter_grade = "B"
elif percentage < 83 and percentage >= 80:
    letter_grade = "B-"
elif percentage < 80 and percentage >= 77:
    letter_grade = "C+"
elif percentage < 77 and percentage >= 73:
    letter_grade = "C"
elif percentage < 73 and percentage >= 70:
    letter_grade = "C-"
elif percentage < 70 and percentage >= 67:
    letter_grade = "D+"
elif percentage < 67 and percentage >= 65:
    letter_grade = "D"
elif percentage < 65 and percentage >= 0:
    letter_grade = "F"
else:
    letter_grade = "Error"
print(letter_grade)

# PROBLEM 2 (Vowels - 5pts)
# Ask the user to supply a string.
# Print how many different vowels there are in the string.
# The capital version of a lower case vowel is considered to be the same vowel.
# y is not considered a vowel.
# Try to print proper output (e.g., printing “There are 1 different vowels in the string” is ugly).
# Example: When the user enters the string “It’s Owl Stretching Time,”
# the program should say that there are 3 different vowels in the string.

user_input = input("Please input a string: ")
a_vowel = False
e_vowel = False
i_vowel = False
o_vowel = False
u_vowel = False

for i in range(len(user_input)):
    if user_input[i].upper() == "A":
        a_vowel = True
    if user_input[i].upper() == "E":
        e_vowel = True
    if user_input[i].upper() == "I":
        i_vowel = True
    if user_input[i].upper() == "O":
        o_vowel = True
    if user_input[i].upper() == "U":
        u_vowel = True
vowel_count = a_vowel + e_vowel + i_vowel + o_vowel + u_vowel
if vowel_count  == 0:
    print("There are no vowels in this string.")
elif vowel_count == 1:
    print("There is one unique vowel in this string.")
else:
    print("There are", vowel_count, "unique vowels in this string.")


# PROBLEM 3 (Quadratic Equation - 6pts)
# You can solve quadratic equations using the quadratic formula.
# Quadratic equations are of the form Ax2 + Bx + C = 0.
# Such equations have zero, one or two solutions.
# The first solution is (−B + sqrt(B^22 − 4AC))/(2A).
# The second solution is (−B − sqrt(B^2 − 4AC))/(2A).
# There are no solutions if the value under the square root is negative.
# There is one solution if the value under the square root is zero.
# Write a program that asks the user for the values of A, B, and C,
# then reports whether there are zero, one, or two solutions,
# then prints those solutions.
# Note: Make sure that you also take into account the case that A is zero,
# and the case that both A and B are zero.

a = float(input("Please enter an A value: "))
b = float(input("Please enter a B value: "))
c = float(input("Please enter a C value: "))

descriminant = b**2 - 4 * a * c


if a == 0 and b == 0:
    if c == 0:
        print("All real numbers.")
    else:
        print("No solution")

elif a == 0:
    print("This is not a quadratic equation.")
    answer = (-1 * c) / b
    print("The answer is:", answer)

elif descriminant == 0:
    print("There is one solution to your equation.")
    answer = (-1 * b) / (2 * a)

elif descriminant > 0:
    print("There are two solutions to your equation.")
    answer = ((-1 * b) + math.sqrt(b**2 - (4*a*c))) / (2 * a)
    print("Solution #1:", answer)
    answer = ((-1 * b) - math.sqrt(b**2 - (4*a*c))) / (2 * a)
    print("Solution #2:", answer)

elif descriminant < 0:
    print("There are 0 real solutions to your equation.")



