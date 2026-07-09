🐍 Python Boot Camp

## Mission 1 – Day 1 ✅

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











## Mission 1 – Day 2 ✅
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

# Mission 1 – Day 4

## Topics Learned

- Random Module
- Lists
- List Indexing
- Parallel Lists
- Importing Modules
- Random Choice
- Random Integer

---

## Random Module

Used to generate random numbers and make random selections.

Functions learned:

random.randint()

Returns a random integer within a given range.

Example:

random.randint(1, 10)

---

random.choice()

Randomly selects one item from a list.

Example:

random.choice(fruits)

---

## Lists

A list stores multiple values in a single variable.

Example:

fruits = ["Apple", "Banana", "Orange"]

Lists are ordered and can be modified.

---

## List Indexing

Python lists start from index 0.

Example:

fruits = ["Apple", "Banana", "Orange"]

fruits[0] → Apple
fruits[1] → Banana
fruits[2] → Orange

Last element:

fruits[len(fruits) - 1]

---

## Parallel Lists

Two or more lists can work together using the same index.

Example:

movies = ["Superman", "F1"]
prices = [250, 300]

movies[0] → Superman
prices[0] → 250

The same index refers to related information.

---

## Things I Learned

- Lists allow storing multiple related values.
- Indexes start from 0.
- User input often needs to be converted to a list index.
- Always validate indexes before accessing a list.
- random.choice() is useful for selecting random items from a list.
- random.randint() generates random numbers within a range.
- Variables should be initialized before use to avoid errors.
- Input validation prevents programs from crashing.
- Build and test programs one step at a time.

---

## Programs Built

- Heads or Tails
- Banker Roulette
- Treasure Map
- Rock Paper Scissors
- Lucky Draw System (Challenge)
- Python Cinema Booking System (Challenge)

---

## Biggest Lesson

A good program doesn't just produce the correct result—it also handles invalid input gracefully and presents the output in a clear, user-friendly way.


# Mission 1 – Day 5

## Topics Learned

- For Loops
- range() Function
- Looping Through Lists
- Modulus Operator in Loops
- Nested Loops
- String Joining
- List Shuffling

---

## For Loops

A for loop is used to repeat a block of code for every item in a sequence.

Example:

for fruit in fruits:
    print(fruit)

---

## range()

The range() function generates a sequence of numbers.

Examples:

range(1, 6)

Produces:

1 2 3 4 5

The ending value is not included.

Step values can also be used.

Example:

range(2, 11, 2)

Produces:

2 4 6 8 10

---

## Modulus Operator

The modulus operator (%) returns the remainder after division.

Examples:

10 % 2 → 0
9 % 3 → 0
7 % 3 → 1

A remainder of 0 means the number is divisible.

---

## Using Loops for Calculations

Variables can be updated inside a loop.

Example:

total += number

This allows calculations like:

- Sum of numbers
- Average
- Counting items

---

## Nested Loops

A loop can exist inside another loop.

Example:

for row in matrix:
    for value in row:
        print(value)

Nested loops repeat the inner loop completely for every iteration of the outer loop.

---

## Lists vs Strings

List

- Mutable
- Items can be added, removed and shuffled.

String

- Immutable
- Cannot be modified after creation.

Choose the correct data structure depending on the task.

---

## random.shuffle()

Shuffles the elements of a list randomly.

Example:

random.shuffle(my_list)

Important:

shuffle() modifies the original list and returns None.

---

## "".join()

Used to combine a list of strings into one string.

Example:

letters = ["H", "e", "l", "l", "o"]

word = "".join(letters)

Output:

Hello

The string before join() becomes the separator.

Examples:

" ".join(list)   → Space separated

"-".join(list)   → Hyphen separated

"".join(list)    → No separator

---

## Things I Learned

- for loops repeat code efficiently.
- range() excludes the ending number.
- The modulus operator is useful for checking divisibility.
- The order of if/elif conditions matters (FizzBuzz).
- Lists are mutable while strings are immutable.
- random.shuffle() changes a list in place.
- Some functions modify objects while others return new values.
- join() returns a new string and does not modify the original list.
- Break large problems into smaller steps before solving them.

---

## Programs Built

- Average Height Calculator
- Highest Score Finder
- Adding Even Numbers
- FizzBuzz
- PyPassword Generator (Easy Level)
- PyPassword Generator (Hard Level)

---

## Biggest Lesson

Understanding *why* a data structure is chosen is more important than memorizing syntax.

Lists are best when data needs to be modified or shuffled.

Strings are best for displaying the final result.