# FitPlan Process Model Comparison

## Waterfall
Work moves through requirements, design, coding, testing, and deployment in order. This is easy to plan, but changes discovered late can cause rework. It could fit FitPlan if requirements were stable.

## Incremental
The system is delivered in small working parts. FitPlan can be built as profile and logging first, then weekly plan generation, then testing and deployment improvements. This lets the team get feedback early.

## Spiral
Each cycle identifies and reduces risks before building the next part. This could help FitPlan focus on risks such as privacy and unsafe generated plans, but it may be too complex for a small student project.

## Prototype
A quick model of the screens or plan flow is created so users can give feedback before the full system is built. This is useful for checking whether FitPlan’s profile and weekly-plan screens make sense, but the prototype still needs proper engineering before release.

## V-Model
Each development stage is paired with a testing stage. For example, requirements connect to acceptance tests and detailed design connects to unit tests. This supports traceability, though changes may be slower to manage.

## Selected model: Incremental
We will use the Incremental model for FitPlan. The project can be divided into manageable parts: first profile and workout/meal logging, then weekly plan generation with validation, then integration, testing, and deployment. Feedback from each part can guide the next increment.

## Mapping to the 28-day project

| Increment or activity | Project days | Main work |
|---|---:|---|
| Plan and design | 1–6 | Set up tools, gather requirements, create diagrams and screen prototype |
| Increment 1 | 7–10 | Plan and begin profile and workout/meal logging |
| Increment 2 | 11–15 | Add weekly plan generation, validation, Docker, and CI/CD work |
| Quality and integration | 16–26 | Test, monitor, review quality, fix defects, and prepare the demo |
| Documentation | 27–28 | Complete the report, presentation, and final evidence |

## Why this fits
Incremental development lets the team build and review one useful part at a time during the short project. It also gives the team a chance to test the plan-validation rules before presenting generated plans to users.
