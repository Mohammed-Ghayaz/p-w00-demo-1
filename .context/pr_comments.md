# PR #1 Review — Calculator Utility (by Arjun Mehta)

## Reviewer: Nisha Gupta — Jan 10, 2026

---

**Overall:** Good structure! But two issues need fixing before merge.

### `calculator.py`

> **subtract method:**
> The operands look swapped. `b - a` gives the opposite sign of what we want.
> Double-check against the docstring.

> **divide method:**
> No zero-check. If someone passes 0 as the divisor, the whole service crashes.
> We need a guard clause.

### `mathUtils.py`

> Looks clean. Ship it.

---

**Arjun Mehta** — Jan 12, 2026

> Got pulled to another project before I could fix these. Leaving for the next person!
