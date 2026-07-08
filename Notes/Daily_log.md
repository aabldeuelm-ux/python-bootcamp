🐍 Python Boot Camp

Mission 1 – Day 1 ✅

Concepts Learned
* print() – Display output to the console.
* input() – Take input from the user.
* Variables – Store values for later use.
* Strings – Text enclosed in quotes.
* String Concatenation – Join strings using +.
* Escape Character \n – Print on a new line.
* len() – Returns the length of a string.

⸻

Programs Built
* Hello World
* Input Practice
* Variables Practice
* Band Name Generator
* Student Card (Bonus Challenge)

⸻

Git Shortcuts
git add .
Stages all changed files for the next commit.
git commit -m "Your message"
Creates a snapshot (commit) of your project.
git push origin main
Uploads your commits to GitHub.
git log --oneline
Shows commit history.
git branch
Displays all branches.
git checkout -b branch-name
Creates a new branch and switches to it.
git checkout main
Switches back to the main branch.
git merge branch-name
Merges another branch into the current branch.
git branch -d branch-name
Deletes a branch after it has been merged.
git commmit --amend -m " "
Changes the Existing commit name 
git push --force origin main
Next step after changing the commit name

⸻

Things to Remember
* Always type the code yourself.
* Experiment with examples.
* Commit after every study session.
* Push your commits to GitHub.
* Ask “Why?”, not just “How?”

⸻

Questions
(Leave this section empty and add any doubts while studying.)

⸻

Mini Cheat Sheet
print("Hello, World!")
name = input("What is your name? ")
print("Hello " + name)
length = len(name)

⸻











Mission 1 – Day 2 ✅
📚 Concepts Learned
1. Primitive Data Types
str   # String (Text)
int   # Integer (Whole numbers)
float # Decimal numbers
bool  # True / False
Examples:
"Hello"
25
3.14
True
False

⸻

2. Type Checking
type(variable)
Example:
print(type("Hello"))   # <class 'str'>
print(type(123))       # <class 'int'>
print(type(12.5))      # <class 'float'>

⸻

3. Type Conversion (Casting)
Convert between data types.
int()
float()
str()
Examples:
age = int("20")
price = float("99.99")
score = str(100)

⸻

4. Mathematical Operators
+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Floor Division
%   Modulus (Remainder)
**  Exponent (Power)
Example:
5 + 2   # 7
5 - 2   # 3
5 * 2   # 10
5 / 2   # 2.5
5 // 2  # 2
5 % 2   # 1
5 ** 2  # 25

⸻

5. Number Manipulation
Useful functions:
round(number, digits)
Examples:
round(3.14159, 2)   # 3.14
round(7.6)          # 8

⸻

6. f-Strings ⭐
Cleaner way to print variables.
Instead of:
print("Hello " + name)
Use:
print(f"Hello {name}")
Benefits:
* Easier to read
* Cleaner code
* Supports calculations inside {}
Example:
print(f"Total = ₹{bill}")

⸻

7. Python Style (PEP 8)
Preferred:
if tip == 10:
Instead of:
if(tip==10):
Always add spaces around operators:
a = b + c
not
a=b+c

⸻

💻 Programs Built
* Data Types Practice
* Type Conversion Practice
* BMI Calculator
* Tip Calculator

⸻

🧠 Biggest Lesson Today
Instead of writing code for specific values:
10
12
15
Write code that works for any value.
Example:
final_bill = (bill * ((tip / 100) + 1)) / people
This works for:
* 10%
* 12%
* 15%
* 18%
* 20%
* 25%
* Any percentage

⸻

💡 Things to Remember
* input() always returns a string.
* Use int() or float() when doing calculations.
* round(value, 2) rounds to two decimal places.
* Use f-strings instead of string concatenation whenever possible.
* Write code that is general, not hardcoded.

⸻

📝 Questions
(Leave this section blank and add any doubts you have.)



✅ Mission 1 – Day 3

## Topics Learned

- Control Flow
- if statements
- elif statements
- else statements
- Comparison Operators
- Logical Operators
- Nested if statements

## Comparison Operators

==
!=
>
<
>=
<=

## Logical Operators

and
or
not

## Nested if

An if statement inside another if statement.

Useful when one decision depends on another.

## Things I Learned

- Programs make decisions using conditions.
- Indentation is important in Python.
- Nested if statements help build decision trees.
- Variables can be modified after initialization.
- Avoid repeating the same code.
- Keep program flow simple and readable.

## Programs Built

- Rollercoaster Ride
- Treasure Island

## Biggest Lesson

Write code that is easy to read before trying to make it clever.
