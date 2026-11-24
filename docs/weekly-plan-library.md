# FitPlan Weekly Plan Prompt Library

**Purpose:** Compare three prompt versions using the same fictional profile. LLM output is untrusted and must be checked by application code before display.

## Shared fictional test profile

- Goal: build a regular fitness routine
- Available days: Monday, Wednesday, Friday, Saturday
- Preference: beginner-friendly activities
- Health conditions: none provided
- Use fictional information only

## Shared rules for all prompt versions

- Create a general weekly activity schedule, not medical advice.
- Include rest days.
- Do not make diagnoses, promise health outcomes, or recommend supplements.
- Do not provide calorie targets or specific nutrition prescriptions.
- If health concerns are mentioned, do not generate a plan; return a message advising the user to consult a qualified professional.
- Return only the requested structured output.
- The application must validate the response and must not show a plan as accepted if validation fails.

## Prompt version A — Basic constraints

> You are helping draft a general fitness schedule for a student project. Use the fictional profile and shared rules in this document. Suggest a simple weekly schedule that reflects the user's available days and preferences, includes rest days, and avoids medical or nutrition prescriptions. Return JSON with `status`, `days`, `activities`, `rest_days`, and `message`. If you cannot follow the rules, set `status` to `needs_review`.

## Prompt version B — Explicit output structure

> Draft a general weekly activity schedule for the fictional profile. Follow all shared rules. Return valid JSON using this structure:
>
> `{ "status": "draft", "days": [{"day": "Monday", "activity": "string", "is_rest_day": false}], "message": "string" }`
>
> Include all seven days. Mark rest days with `is_rest_day: true`. Do not add fields or text outside the JSON. If health concerns are present or you cannot follow a rule, return `{"status":"needs_review","days":[],"message":"Please consult a qualified professional."}`.

## Prompt version C — Checklist before responding

> Draft a general weekly activity schedule for the fictional profile. Before returning the result, check that it:
>
> 1. Uses only the provided goal, available days, and preference.
> 2. Includes seven days and at least one rest day.
> 3. Contains no diagnosis, medical claim, supplement advice, calorie target, or nutrition prescription.
> 4. Uses the exact JSON structure from Prompt version B.
> 5. Returns `needs_review` instead of a plan if health concerns are present.
>
> Return only the JSON result. The application will independently validate every field and rule.

## Prompt comparison record

Complete this after trying all three versions with the same profile.

| Version | Output saved? | Followed requested format? | Followed constraints? | Problems found | Keep, edit, or reject |
|---|---|---|---|---|---|
| A | Not tried | Not checked | Not checked |  |  |
| B | Not tried | Not checked | Not checked |  |  |
| C | Not tried | Not checked | Not checked |  |  |

## Review note

A prompt does not make a plan safe by itself. The backend must validate the response using rules approved for the project before displaying it.
