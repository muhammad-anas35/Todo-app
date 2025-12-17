---
name: technical-clarity
version: 1.0.0
description: Ability to explain complex technical concepts with absolute clarity, avoiding jargon where possible, and using analogies when helpful.
---

## Capabilities

### 1. Concept Simplification
- **Goal**: Make architecture accessible to junior developers.
- **Method**: Break down "Why" before "How".
- **Pattern**:
  1.  **Analogy**: "Think of Protocols like a plug socket..."
  2.  **Definition**: "Technically, it defines a structural type..."
  3.  **Application**: "In this project, we use it for Storage..."

### 2. Jargon Management
- **Rule**: Never use an acronym (DI, SRP, OCP) without first defining it in context.
- **Example**: "Dependency Injection (DI) - passing the database to the manager instead of creating it inside."

## Usage
- Invoke when explaining architectural decisions.
- Invoke when writing documentation strings.
