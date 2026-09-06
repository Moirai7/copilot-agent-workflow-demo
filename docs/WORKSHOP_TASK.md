# Scenario B — Software Change Request

## Engineering request

Add input validation to the existing `POST /temperature` endpoint without breaking current behavior.

## Acceptance criteria

| Input | Expected |
|---|---|
| `{"value": 72}` | HTTP 200 |
| `{"value": 72.5}` | HTTP 200 |
| `{}` | HTTP 400 |
| `{"value": "hot"}` | HTTP 400 |
| `{"value": -101}` | HTTP 400 |
| `{"value": 201}` | HTTP 400 |
| `{"value": -100}` | HTTP 200 |
| `{"value": 200}` | HTTP 200 |

## Constraints
- Make the smallest reasonable change.
- Preserve existing valid behavior.
- Do not modify unrelated files.
- Add tests for new behavior.
- A human reviews the plan before implementation.
- A human reviews the final diff, tests, and review findings before merge.
