# ADR-001: Calculator Utility Design

**Date:**
**Status:** Accepted
**Authors:** Nisha Gupta

## Decision

We use a single `Calculator` class with history tracking rather than standalone functions.

## Context

Multiple services need basic arithmetic. Instead of each team writing their own, we centralize it.

## Rationale

- History tracking helps with audit logging
- Class-based design allows easy extension
- Separating math utilities (`mathUtils.py`) from the calculator keeps concerns clean

## Structure

```
src/
  calculator.py  â€” Main Calculator class (the one you fix)
  mathUtils.py   â€” Helper functions (already correct)
tests/
  test_calculator.py â€” Tests to verify your fixes
```
