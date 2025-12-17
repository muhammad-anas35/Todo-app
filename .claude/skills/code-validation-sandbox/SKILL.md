---
name: code-validation-sandbox
version: 1.0.0
description: Strategies for verifying code correctness through execution and manual testing plans.
---

## Capabilities

### 1. Manual Test Scripts
- **Purpose**: verify CLI interactivity which is hard to unit test.
- **Format**: Step-by-step instructions.
- **Example**:
  1. Run `python -m src`
  2. Input `1` (Add Task)
  3. Input `Test Task`
  4. Verify output "Task added"

### 2. Smoke Testing
- **Definition**: Basic non-exhaustive set of tests that verify major functions.
- **Trigger**: Run on every major refactor.

### 3. Edge Case Discovery
- **Strategy**: Boundary value analysis (Min/Max inputs).
- **Strategy**: Invalid input types (Letters where numbers expected).

## Usage
- Invoke to generate the `Verification Plan` section of `plan.md`.
- Invoke to troubleshoot "It works on my machine" issues.
