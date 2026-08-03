# C690 Author Release QA

Date: 3 August 2026  
Courseware version: v1.0  
n8n registry stable version observed during authoring: 2.32.7 (not runtime-tested)  

This record covers static JSON validation only and separates checks that can be completed without a model credential from the credentialed live preflight that the trainer must complete in the delivery workspace. It is not a learner answer key.

## Completed Static Release Checks

| Check | Result | Evidence |
|---|---|---|
| Both starter JSON files parse | PASS | `python labs/resources/validate_n8n_starters.py` |
| Required n8n node types and connections exist | PASS | 4-node Lab 3 starter; 5-node Lab 4 reference with Calculator tool connection |
| Shareable workflows are inactive and Chat Trigger is not public | PASS | `active=false`; Chat Trigger `public=false` in both starters |
| Starter files contain no credential object | PASS | Recursive key check in `validate_n8n_starters.py` |
| Action-status labels match the test CSV and templates | PASS | Eight-label contract checked in both workflow prompts |
| Sanitizer removes credential references and forces safe release flags | PASS | Both starters returned `SANITIZED OK`; outputs reported `active=false` and Chat Trigger `public=false` |
| Ten required regression rows are uniquely identified | PASS | B01-B03, T01-T03, and S01-S04; F01 is clearly optional |

## Trainer Live Preflight — Required Before Any Controlled Demo

Status at author release: `PENDING DELIVERY WORKSPACE`  
Reason: a trainer-approved n8n workspace and model credential are intentionally not embedded in or supplied with the courseware.

The trainer must complete and retain the following in `04-tool-tests-and-deployment-record.md`:

- n8n version and model/provider used;
- Lab 3 import, credential selection, four baseline results, execution inspection, sanitized export, and sanitized re-import;
- Lab 4 duplication from verified v1.0, the allowed v1.1 diff, and all ten MUST-PASS results;
- restricted-authentication Publish test, Unpublish time, and failed access from a private browser session;
- final reset to `active=false` and Chat Trigger `public=false`, followed by final diff, sanitizer, and re-import checks.

Release rule: the courseware may be distributed for trainer-led practice, but the workflow decision remains `HOLD` until the live preflight evidence is complete. No public endpoint or credential is present in this repository.
