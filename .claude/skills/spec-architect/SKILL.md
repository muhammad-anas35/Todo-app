---
name: spec-architect
version: 1.0.0
description: specialized in writing clear, testable, and comprehensive Markdown specifications for software features.
---

## Capabilities

### 1. Requirement Structuring
- **Format**: Functional Requirements (FR) and User Stories (US).
- **ID System**: `FR-001`, `US-01`. All requirements must be indexed.
- **Traceability**: `[Source: US-01]` tags on FRs.

### 2. Document Hierarchy
- **Level 1**: `spec.md` (The "What" - Requirements).
- **Level 2**: `plan.md` (The "How" - Technical Solution).
- **Level 3**: `tasks.md` (The "When" - Execution Steps).

### 3. Gherkin-Style Scenarios
- **Pattern**: Given/When/Then.
- **Usage**: Mandatory for Acceptance Criteria.
- **Example**:
  > **Given** the task list is empty
  > **When** I request to View All Tasks
  > **Then** I see a "No tasks found" message

## Usage
- Invoke whenever a new feature is requested.
- Invoke to validate if a proposed code change triggers a spec update.
