# FitPlan Requirements Draft

**Status:** Initial draft for review  
**Project:** FitPlan Fitness and Diet Planner

## Purpose
FitPlan is a student project for recording user profiles, workouts, and meals, and generating a personalized weekly fitness plan for review.

## Users
- **User:** Manages their profile and personal logs and requests a weekly plan.
- **Trainer:** Reviews information only when the user chooses to share it.

## Functional requirements
- **FR-01:** The system shall let a user create and update a profile.
- **FR-02:** The system shall let a user record and view workout entries.
- **FR-03:** The system shall let a user record and view meal entries.
- **FR-04:** The system shall let a user enter fitness goals, available days, and relevant preferences for plan generation.
- **FR-05:** The system shall request a weekly plan from the configured language model.
- **FR-06:** The system shall check the generated plan against documented application rules before displaying it.
- **FR-07:** The system shall reject malformed or rule-breaking plans and show a clear message.
- **FR-08:** The system shall label accepted plans as AI-generated.
- **FR-09:** The system shall limit trainer access to information the user has chosen to share.
- **FR-10:** The system shall let a user request deletion of their project data.

## Quality requirements
- **QR-01:** The project shall aim for at least 80% automated test coverage.
- **QR-02:** The team shall test 30 fictional profiles against all 10 documented plan checks.
- **QR-03:** API keys and passwords shall not be stored in the public repository.
- **QR-04:** Tests and examples shall use fictional profile information.
- **QR-05:** The application shall explain when a plan cannot be generated or fails validation.

## Safety and privacy notes
- FitPlan is a student project and does not provide medical advice, diagnosis, or treatment.
- The application shall not display a plan that fails its configured validation rules.
- Numeric nutrition limits and other health-related rules need to be confirmed with the instructor and an appropriately qualified professional before implementation.
- Users with health concerns shall be directed to consult a qualified professional.

## Open questions
- Which profile fields are required for the class prototype?
- What exact 10 validation checks will the team implement, and who will approve them?
- What trainer permissions are needed?
- Which LLM provider is approved for the project?
- What data should be retained, and how should deletion work?

## Review record
Add the real interview or role-play date, participant role, feedback, and changes after collecting them. Do not invent interview results.
