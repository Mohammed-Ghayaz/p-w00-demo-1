# ADR-001: Calculator Utility Design

**Date:** 2025-11-01
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

`
src/
  calculator.py  — Main Calculator class (the one you fix)
  mathUtils.py   — Helper functions (already correct)
tests/
  test_calculator.py — Tests to verify your fixes
`
"@ | Set-Content "c:\Users\DINESH VA\Desktop\SDE tivor\Product-Track\Demo\Demo-1\docs\DESIGN.md" -Encoding UTF8

# ===== tests/test_calculator.py =====
@"
"""
Tests for Calculator Utility.
Run with: python -m pytest tests/ -v
"""

import pytest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator


class TestCalculator:
    def test_add(self):
        calc = Calculator()
        assert calc.add(2, 3) == 5

    def test_add_negative(self):
        calc = Calculator()
        assert calc.add(-1, -2) == -3

    def test_subtract(self):
        calc = Calculator()
        assert calc.subtract(10, 3) == 7, "subtract(10, 3) should return 7"

    def test_subtract_negative_result(self):
        calc = Calculator()
        assert calc.subtract(3, 10) == -7, "subtract(3, 10) should return -7"

    def test_multiply(self):
        calc = Calculator()
        assert calc.multiply(4, 5) == 20

    def test_divide(self):
        calc = Calculator()
        assert calc.divide(10, 2) == 5

    def test_divide_by_zero(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.divide(10, 0)

    def test_history(self):
        calc = Calculator()
        calc.add(1, 2)
        calc.multiply(3, 4)
        history = calc.get_history()
        assert len(history) == 2
        assert history[0]['op'] == 'add'
        assert history[1]['op'] == 'multiply'

    def test_clear_history(self):
        calc = Calculator()
        calc.add(1, 1)
        calc.clear_history()
        assert len(calc.get_history()) == 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
