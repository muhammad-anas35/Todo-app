---
name: frontend-design
version: 1.0.0
description: Expertise in CLI user experience, visual hierarchy, and terminal interface design.
---

## Capabilities

### 1. Visual Hierarchy
- **Principle**: Use whitespace to group related information.
- **Header**: Standard 50-char width double-line border.
- **Footer**: Action prompts separated by a single divider line.

### 2. Color Theory (Terminal)
- **Constraint**: Assume standard 16-color ANSI palette.
- **Semantics**:
  - `Red`: Errors, Destructive actions (Delete).
  - `Green`: Success, Safe actions (`✓`).
  - `Yellow`: Warnings, Important notes.
  - `Cyan`: Headers, Section titles.
  - `Reset`: Normal text.

### 3. User Feedback Loops
- **Confirmation**: Always confirm state changes.
- **Transitions**: Clear screen between major context switches (Main Menu -> Add Task).

## Style Guide
- **Indentation**: 2 spaces for list items.
- **Prompts**: `[?] Question: ` or `> Input: `
