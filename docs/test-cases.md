# FitPlan Profile and Workout Test Cases

**Status:** Planned; execution results not recorded yet  
**Test data:** Use fictional profiles only.

| ID | Requirement | Test | Expected result | Result |
|---|---|---|---|---|
| TC-P01 | FR-01 | Create a profile with valid sample details. | Profile is saved and can be viewed. | Not run |
| TC-P02 | FR-01 | Update a profile preference and save. | Updated preference appears when the profile is viewed again. | Not run |
| TC-P03 | FR-01 | Leave a required profile field empty. | The form explains what needs to be corrected. Confirm which fields are required before implementation. | Not run |
| TC-P04 | Proposed access rule | Try to view another user’s profile without permission. | Access is denied. Confirm this rule with the team. | Not run |
| TC-P05 | Proposed validation rule | Enter an invalid value in a profile field. | The form shows a helpful validation message. Define invalid values with the team. | Not run |
| TC-W01 | FR-02 | Add a workout with valid fictional details. | Workout is saved and appears in the user’s history. | Not run |
| TC-W02 | FR-02 | Open workout history after saving an entry. | The saved workout details are displayed. | Not run |
| TC-W03 | Proposed validation rule | Submit a workout without an activity name. | The form asks for the missing information. Confirm required fields with the team. | Not run |
| TC-W04 | Proposed validation rule | Enter a zero or negative workout duration. | The form rejects the value with a clear message. Confirm the duration rule with the team. | Not run |
| TC-W05 | Proposed access rule | Try to view another user’s workout without permission. | Access is denied. Confirm this rule with the team. | Not run |

## Notes

- “Proposed” rules are suggestions and need team approval before they become requirements.
- Record actual results, defects, and dates only after running each test.
  
