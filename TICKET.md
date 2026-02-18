# DEMO-001: Fix the Calculator Utility

**Status:** In Progress · **Priority:** Low
**Sprint:** Onboarding Sprint · **Story Points:** 1
**Reporter:** Nisha Gupta (Tech Lead) · **Assignee:** You (New Intern)
**Due:** No rush — this is your first task!
**Labels:** `onboarding`, `python`, `beginner`
**Task Type:** Bug Fix

---

## 👋 Welcome to Your First Task!

This is a **preview** of how tasks work in the SDE Intern Simulator. Don't worry — this one
is designed to be easy. The goal is to get comfortable with the workflow:

1. Read this ticket (you're doing it now ✅)
2. Look at the code in `src/`
3. Find the bugs (they're marked with `# BUG:` comments)
4. Fix them
5. Run the tests to verify

## Description

The team's internal calculator utility has two bugs that were introduced during a refactor.
The `subtract` and `divide` methods aren't working correctly. Your job is to fix them.

## Acceptance Criteria

- [ ] `subtract(10, 3)` returns `7` (not `-7`)
- [ ] `divide(10, 0)` raises `ValueError` (not crashes the app)
- [ ] All existing tests pass
- [ ] You've added at least 1 new test

## Design Notes

See `docs/GUIDE.md` for a Python crash course if you need it.
See `docs/DESIGN.md` for the calculator architecture.
