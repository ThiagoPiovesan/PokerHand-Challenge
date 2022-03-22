# Poker hand Rank:
---
## Concepts used:
- TDD;
- SOLID;
- Design Patterns.

---

## Objective:
The main purpose of these is to compare two poker hands and print who is the winner. Very simple, right?
No, actually we want to show the usability of the concepts shown earlier and apply then into a simple problem.
So, let's get it started!

---

## How does it work?
Using the main.py program, we give "two poker hands" as input. Like this:

- hand1 = "9C 9H 5C 5H AC"
- hand2 = "TC TH 5C 5H KH"

---

## A little of theory and concepts included (You can skip if you want to):

### SOLID Concept:
#### # Single responsibility principle:
→ Make things (classes, functions, etc.) responsible for fulfilling one type of role.
—> **e.g**. Refactor code responsibilities into separate classes.

#### # Open/Closed:
→ Be able to add new functionality to existing code easily without modifying existing code.
—> **e.g**. Use abstract classes. These can define what subclasses will require and strengthen Principle by separating code duties.

#### # Liskov Substitution:
→ When a class inherits from another class, the program shouldn't break and you shouldn't need to hack anything to use the subclass.
—> **e.g**. Define constructor arguments to keep inheritance flexible.

#### # Interface Segregation:
→ Make interfaces (parent abstract classes) more specific, rather than generic.
—> **e.g**. Create more interfaces (classes) if needed and/or provide objects to constructors.

#### # Dependency Inversion:
→ Make classes depend on abstract classes rather than non-abstract classes.
—> **e.g**. Make classes inherit from abstract classes.

---

### TDD (Test-Driven Develop):
→ “**Write the test, before write de actual code”**.

---

**# Step 1: Write tests**
→ Start by writing the tests that only pass if the feature specifications are met.
→ Forces you to think about the requirements before actual starts building something.

**# Step 2: Run the tests**
→ Running those tets and make sure they all fail;
→ Check that you’re actually adding something new and that the tests are properly testing that part.

**# Step 3: Write the actual code**
→ Write the simplest code so that these tests pass;
→ Doesn’t need to be perfect, just new to met the specifications.

**# Step 4: Make All tests pass**
→ Make sure that all tests now pass;
→ Including any other older tests that you have this ensures that the new features adheres to the specifications and it doesn’t break other things 

**# Step 5: Refactoring and Improving**
→ Refactoring and Improving the code while you have the test harness running.

---                              

                                                    **RED → GREEN → REFACTOR**

---

→ Don’t use global instances, that way a test can’t interfere on the other
→ Don’t tests python standard library stuff, it is expected to work correctly.

---
## Thanks for the read & I hope you enjoy it!

> To get started/contribute (if you want - optional) ...

- **Option 1**
    - 🍴 Fork this repo and pull request!

- **Option 2**
    - 👯 Clone this repo: 
    ```
    $ git clone https://github.com/ThiagoPiovesan/PokerHand-Challenge.git
    ```

- **Enjoy it!**

---

Ass: Thiago Piovesan - 03/2022 -- version: 1.0.0.