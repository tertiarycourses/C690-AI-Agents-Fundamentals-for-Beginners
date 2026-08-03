# BrightDesk Workspace - Synthetic Agent Brief

This scenario is fictional and contains no real customer, employee, payment, or confidential information.

## Organisation

BrightDesk Workspace operates a fictional shared workspace in Singapore. It offers day passes, meeting rooms, and training rooms. The customer-experience team answers questions through web chat and confirms all bookings manually.

## Intended user

A prospective visitor who wants to understand published services, opening hours, visitor rules, facilities, or a non-binding price estimate before contacting staff.

## Business need

The team receives repetitive questions in different wording. It wants a beginner-friendly demonstration agent that can:

- answer only from the approved BrightDesk FAQ;
- cite the relevant FAQ section ID;
- calculate a transparent estimate using source-backed rates and durations;
- state uncertainty when the source is silent or conflicting; and
- hand booking, availability, discount, payment, complaint, safety, and personal-data matters to staff.

## Supported demonstration

The course agent may use a chat interface, short-term session memory, the supplied FAQ, and a Calculator tool. It may produce an answer, a non-binding estimate, or a draft handoff packet.

## Human owner

The BrightDesk Customer Experience Lead owns source accuracy, public wording, handoffs, and any decision to publish the demonstration.

## Constraints

- The course workflow uses synthetic data only.
- It does not confirm availability, create a booking, take payment, send an external message, update a record, or provide an unlisted discount.
- It does not request or retain passwords, API keys, identity documents, payment details, health information, or real customer records.
- A friendly persona never changes the agent's evidence or authority boundary.
- Any public test must be easy to pause and must have a recorded rollback path.

## Observable result

A supported question produces a concise answer with a valid FAQ section ID. A supported numeric request produces a transparent, non-binding estimate. An unsupported or consequential request stops with a clear reason and a staff handoff.

