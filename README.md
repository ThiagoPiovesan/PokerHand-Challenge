# Poker hand Rank:
---

## Objective:
→ The main purpose of these project, is to compare two poker hands and print who is the winner. Very simple, right?<br />

→ No, actually we want to show the usability of the concepts below and apply then into a simple problem.<br />
→ So, let's get it started!

#### Concepts used:
- TDD;
- SOLID;
- Design Patterns.

---

## How does it work?
→ Inside the PokerHand archive we have the file **PokerHand**, where is the principal class and where is the *compare_with* method that really compare the two hands. Of course, this class only do this specific job, compare the two hands e return who win.<br />
→ So, we have two more files e classes. CardsControl archive has the **OrganizeCards** file, which is responsible to get the entering information and extract it into a specific structure.<br />
→ Finally, we have the **EvaluateCards** program. This file gets the structure sent for **OrganizeCards** and make the punctuation and the combination of those cards (e.g. Flush, pair, two pair etc).<br />

→ So, to simplify the usability, we can use the main.py program on root folder. We just need to give "two poker hands" as input. Like this:

- hand1 = "9C 9H 5C 5H AC"
- hand2 = "TC TH 5C 5H KH"

→ Use the function compare_with and *voilà* we have which is the hand winner as result.<br />

→ If you want to, in each folder has all the classes used and code written to use and adapt to your necessity. In addition, has the tests file, which has all the tests (TDD) develop for each class, to make sure they are working well.<br />

→ Or, below has all the theory used and implemented on this challenge, make your self free to read and understand it.<br />

---
## A little of theory and concepts included (You can skip if you want to):

<details>
  <summary>SOLID Concept</summary>
  
#### # Single responsibility principle:
→ Make things (classes, functions, etc.) responsible for fulfilling one type of role.<br />
→ **e.g**. Refactor code responsibilities into separate classes.<br />

#### # Open/Closed:
→ Be able to add new functionality to existing code easily without modifying existing code.<br />
→ **e.g**. Use abstract classes. These can define what subclasses will require and strengthen Principle by separating code duties.<br />

#### # Liskov Substitution:
→ When a class inherits from another class, the program shouldn't break and you shouldn't need to hack anything to use the subclass.<br />
→ **e.g**. Define constructor arguments to keep inheritance flexible.<br />

#### # Interface Segregation:
→ Make interfaces (parent abstract classes) more specific, rather than generic.<br />
→ **e.g**. Create more interfaces (classes) if needed and/or provide objects to constructors.<br />

#### # Dependency Inversion:
→ Make classes depend on abstract classes rather than non-abstract classes.<br />
→ **e.g**. Make classes inherit from abstract classes.<br />

</details>

---

<details>
  <summary>TDD (Test-Driven Develop)</summary>
  
→ “**Write the test, before write de actual code”**.

---

**# Step 1: Write tests**<br />
→ Start by writing the tests that only pass if the feature specifications are met.<br />
→ Forces you to think about the requirements before actual starts building something.<br />

**# Step 2: Run the tests**<br />
→ Running those tets and make sure they all fail;<br />
→ Check that you’re actually adding something new and that the tests are properly testing that part.<br />

**# Step 3: Write the actual code**<br />
→ Write the simplest code so that these tests pass;<br />
→ Doesn’t need to be perfect, just new to met the specifications.<br />

**# Step 4: Make All tests pass**<br />
→ Make sure that all tests now pass;<br />
→ Including any other older tests that you have this ensures that the new features adheres to the specifications and it doesn’t break other things. <br />

**# Step 5: Refactoring and Improving**<br />
→ Refactoring and Improving the code while you have the test harness running.<br />

---                              

                                          RED → GREEN → REFACTOR

---

**Tips:** <br />
→ Don’t use global instances, that way a test can’t interfere on the other<br />
→ Don’t tests python standard library stuff, it is expected to work correctly.<br />

</details>

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