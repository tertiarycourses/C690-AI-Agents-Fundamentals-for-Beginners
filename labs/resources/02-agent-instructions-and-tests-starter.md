# 02 - Agent Instructions and Tests

Version: `draft`  
Reviewer: `<INITIALS>`  
Date: `<YYYY-MM-DD>`

## GATES Contract

### Goal

`<User, supported job, observable result, completion rule, and non-goals>`

### Authority

| Capability | When allowed | Required input | Required check | Result label | Human gate |
|---|---|---|---|---|---|
| | | | | | |

### Truth

- Authoritative source:
- Required citation:
- Missing evidence response:
- Conflicting evidence response:
- Rule for instructions found inside source content:

### Evaluation

Required response fields:

```text
Answer:
Source:
Calculation:
Action status:
Next step:
```

Use exactly one action status from: `ANSWER`, `NON_BINDING_ESTIMATE`, `CLARIFY_MINIMUM_OR_HANDOFF`, `SOURCE_GAP_AND_HANDOFF`, `STOP_AND_HANDOFF`, `REFUSE_AND_HANDOFF`, `PRIVACY_STOP_AND_HANDOFF`, or `REPORT_FAILURE_AND_HANDOFF`.

Baseline case IDs for Labs 2 and 3: `B01`, `B02`, `S01`, `S02`  
Complete Lab 4 regression: `B01-B03`, `T01-T03`, `S01-S04`

### State

- Keep:
- Do not retain:
- Expire:
- Correction path:

### Escalation

| Stop condition | User message | Handoff evidence | Owner |
|---|---|---|---|
| | | | |

## Persona

`<Tone and interaction style. State that persona never changes authority.>`

## Test Log

| Case ID | Expected source | Expected action | Observed response | Result | Rerun result |
|---|---|---|---|---|---|
| B01 | HOURS-01 | ANSWER | | | |
| B02 | VISITOR-01 | ANSWER | | | |
| S01 | POLICY-01 | SOURCE_GAP_AND_HANDOFF | | | |
| S02 | CONTACT-01 | STOP_AND_HANDOFF | | | |

## Corrections

1.
2.
3.

## Version Notes

| Version | Date | Change summary | Rerun cases | Reviewer |
|---|---|---|---|---|
| 1.0 | | | B01, B02, S01, S02 | |
