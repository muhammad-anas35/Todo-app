---
name: visual-asset-workflow
version: 1.0.0
description: Manages the usage of non-text visual elements in the CLI, including ASCII art and icons.
---

## Capabilities

### 1. Iconography
- **Verified Set**: The only safe cross-platform icons.
  - Check: `✓` (U+2713)
  - Circle: `○` (U+25CB)
  - Cross: `❌` (U+274C) - *Use with caution on Windows legacy cmd*
  - Warning: `⚠` (U+26A0)

### 2. ASCII Header Generation
- **Tool**: Use standard Figlet fonts if available, or simple box-drawing manual creation.
- **Constraint**: Max width 80 chars.

### 3. Tables
- **Format**: Simple aligned text or Markdown-style tables.
- **Example**:
  ```text
  ID  | Status | Title
  ----|--------|----------------
  1   |   ✓    | Buy Milk
  2   |   ○    | Walk Dog
  ```

## Usage
- Invoke when designing "View" screens or "Welcome" messages.
