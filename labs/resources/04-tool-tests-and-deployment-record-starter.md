# 04 - Tool Tests and Deployment Record

Workflow: `C690 - BrightDesk Tool Agent - v1.1`  
n8n version: `<VERSION>`  
Model provider/model: `<PROVIDER / MODEL>`  
Instruction version: `1.1`  
Knowledge version: `1.0`  
Reviewer/date: `<INITIALS> / <YYYY-MM-DD>`

## Ten-Case Regression

| Case ID | Expected source | Calculator expected | Calculator observed | Inputs/output | Action status | Result/rerun |
|---|---|---|---|---|---|---|
| B01 | HOURS-01 | NO | | | ANSWER | |
| B02 | VISITOR-01 | NO | | | ANSWER | |
| B03 | FACILITY-01 | NO | | | ANSWER | |
| T01 | PRICE-01 | YES | | | NON_BINDING_ESTIMATE | |
| T02 | PRICE-01 | NO | | | CLARIFY_MINIMUM_OR_HANDOFF | |
| T03 | PRICE-02 | YES | | | NON_BINDING_ESTIMATE | |
| S01 | POLICY-01 | NO | | | SOURCE_GAP_AND_HANDOFF | |
| S02 | CONTACT-01 | NO | | | STOP_AND_HANDOFF | |
| S03 | SECURITY-01 | NO | | | REFUSE_AND_HANDOFF | |
| S04 | VISITOR-01 | NO | | | PRIVACY_STOP_AND_HANDOFF | |

## Version Diff Review

Allowed differences: Calculator node and connection; Calculator permission text; v1.1 name/version metadata.

| Difference | Allowed | Reviewer note |
|---|---|---|
| | | |

- New trigger: `NO / HOLD`
- Selected credential in sanitized export: `NO / HOLD`
- External tool: `NO / HOLD`
- Public setting before approval: `NO / HOLD`
- Final Chat Trigger `public` value after containment: `false / HOLD`
- Reviewer/date:

## Publish or Hold Decision

Decision: `READY FOR CONTROLLED DEMO / HOLD - <CASE OR REASON>`  
Approver:  
Authentication: `TRAINER-RESTRICTED / NOT PUBLISHED`  
Published URL or `N/A`:  
Publish time or `N/A`:  
Unpublish time or `N/A`:  
Failed access after Unpublish: `CONFIRMED / NOT RUN / HOLD`

## Operating Record

- Owner:
- Source review date:
- Permitted tool:
- Support channel:
- Monitoring checks:
- Error threshold:
- Next review date:
- Pause method: `Unpublish`
- Credential revoke method:
- Rollback target: `C690-BrightDesk-Knowledge-Agent-v1.0.json`

## Final Manifest

- [ ] 01-use-case-and-agent-canvas.md
- [ ] 02-agent-instructions-and-tests.md
- [ ] 03-build-and-baseline-test-log.md
- [ ] C690-BrightDesk-Knowledge-Agent-v1.0.json (sanitized and re-imported)
- [ ] 04-tool-tests-and-deployment-record.md
- [ ] C690-BrightDesk-Tool-Agent-v1.1.json (sanitized and re-imported)
