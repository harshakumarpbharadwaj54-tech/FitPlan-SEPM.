# AI Review of FitPlan Requirements

**Status:** Preliminary review of the requirements draft  
**Important:** These are review suggestions, not interview findings. Confirm decisions with the team and instructor.

| Finding | Suggested action | Check before accepting |
|---|---|---|
| The draft does not define who can view or edit each workout and meal entry. | Add an ownership rule: users can access only their own entries unless they explicitly share them. | Confirm whether trainers need any additional permissions. |
| Goals, available days, and preferences are not yet defined as specific inputs. | List the fields the prototype will collect and make each field understandable to users. | Confirm the fields with your classmate and instructor. |
| The draft does not say what happens if the LLM is unavailable or returns unreadable output. | Add a requirement to show a clear error and not display an invalid plan as accepted. | Test a timeout and malformed response later. |
| “Documented application rules” is not specific enough to implement yet. | Write the 10 plan checks and record who approves them before coding. | Numeric health-related limits need instructor and qualified-professional review. |
| The plan review and acceptance flow is unclear. | Show the plan as a draft until validation passes; label it as AI-generated. | Confirm the wording and what users can do with a rejected draft. |
| Trainer sharing needs more detail. | Specify how a user grants, changes, and withdraws sharing permission. | Confirm the expected trainer workflow. |
| Data deletion is mentioned, but its scope is unclear. | Define which profile, log, and plan records are removed when deletion is requested. | Confirm any course or database constraints. |
| Privacy and security requirements are too broad. | Add requirements for authentication, secret storage, and fictional test data. | Check the implementation and repository for exposed secrets. |
| The 80% coverage goal does not specify how it will be measured. | State that coverage will be recorded from the automated test report. | Save the actual report when tests are run. |
| “30 profiles pass all 10 checks” needs a clear test record. | Create a 30-profile test matrix with pass/fail results for each defined check. | Do not claim the target is met until the tests have been run. |

## Decisions

- Add clear access-control, error-handling, sharing, and deletion requirements to the next SRS version.
- Keep the 10 plan checks and numeric health-related limits open until they are reviewed.
- Replace any sample interview answers with actual classmate role-play notes before treating them as user input.
