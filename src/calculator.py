"""
Calculator Utility — basic arithmetic operations.

This is the team's internal calculator used by other services.
Your job: find and fix the bugs marked with # BUG: comments.

Author: Arjun Mehta (previous intern)
Last Modified: 2026-01-15
"""


class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        result = a + b
        self._record('add', a, b, result)
        return result

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a. Example: subtract(10, 3) should return 7."""
        # BUG: The operands are in the wrong order.
        # b - a gives -7 when we want 10 - 3 = 7.
        result = b - a
        self._record('subtract', a, b, result)
        return result

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        result = a * b
        self._record('multiply', a, b, result)
        return result

    def divide(self, a: float, b: float) -> float:
        """Divide a by b. Should raise ValueError if b is zero."""
        # BUG: No check for division by zero.
        # When b is 0, Python raises ZeroDivisionError which crashes the caller.
        # We should catch this and raise a friendly ValueError instead.
        result = a / b
        self._record('divide', a, b, result)
        return result

    def _record(self, operation: str, a: float, b: float, result: float):
        """Record operation in history."""
        self.history.append({
            'op': operation,
            'a': a,
            'b': b,
            'result': result,
        })

    def get_history(self):
        """Return a copy of the operation history."""
        return list(self.history)

    def clear_history(self):
        """Clear all history."""
        self.history.clear()
