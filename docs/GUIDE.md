# Learning Guide — Python Basics

> **Welcome to Demo Task 1!**
> This guide teaches you everything you need to fix the bugs in `calculator.py`.
> If you already know Python, skip ahead to "Bugs to Fix" at the bottom.

---

## What You Need To Do

1. **Read** `TICKET.md` — understand the task
2. **Read** this guide — learn the Python you need
3. **Open** `src/calculator.py` — find the `# BUG:` comments
4. **Fix** the two bugs
5. **Run tests:** `python -m pytest tests/ -v`

---

## Python Quick Reference

### Variables
`python
name = "Alice"        # string
age = 25              # integer
price = 9.99          # float
is_active = True      # boolean
`

### Functions
`python
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")  # "Hello, Alice!"
`

### Classes
`python
class Dog:
    def __init__(self, name):
        self.name = name         # 'self' = this object

    def bark(self):
        return f"{self.name} says Woof!"

dog = Dog("Rex")
print(dog.bark())  # "Rex says Woof!"
`

### Error Handling
`python
try:
    result = 10 / 0
except ZeroDivisionError:
    raise ValueError("Can't divide by zero!")
`

### Lists
`python
items = [1, 2, 3]
items.append(4)     # [1, 2, 3, 4]
items.clear()       # []
`

---

## Bugs to Fix

### Bug #1: `subtract` method
**What's wrong:** The operands are reversed — `b - a` instead of `a - b`
**Where:** `src/calculator.py`, line with `# BUG:` comment
**Fix:** Swap `b - a` to `a - b`

### Bug #2: `divide` method
**What's wrong:** No check for division by zero — crashes instead of raising ValueError
**Where:** `src/calculator.py`, line with `# BUG:` comment
**Fix:** Add `if b == 0: raise ValueError(...)` before the division

---

## How to Run Tests

`ash
cd Demo/Demo-1
python -m pytest tests/ -v
`

You should see all tests pass after fixing both bugs.
