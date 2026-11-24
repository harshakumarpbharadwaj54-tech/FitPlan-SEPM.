# FitPlan Design Diagrams

## Use-case view

```mermaid
flowchart LR
    User[FitPlan user]
    Trainer[Trainer]

    subgraph FitPlan
        Profile[Create or update profile]
        Workout[Log and view workouts]
        Meal[Log and view meals]
        Request[Request weekly plan]
        Validate[Validate generated plan]
        View[View accepted plan]
        Share[Choose information to share]
        Review[Review shared information]
    end

    User --> Profile
    User --> Workout
    User --> Meal
    User --> Request
    Request --> Validate
    Validate --> View
    User --> Share
    Share --> Review
    Trainer --> Review
```

The user manages their profile and personal logs and requests a weekly plan. The trainer can review only information the user chooses to share. The application validates a generated plan before displaying it.

## Data model

```mermaid
erDiagram
    USER ||--|| PROFILE : has
    USER ||--o{ WORKOUT : records
    USER ||--o{ MEAL : records
    USER ||--o{ WEEKLY_PLAN : requests
    WEEKLY_PLAN ||--|{ PLAN_ITEM : contains

    USER {
        int id PK
        string email
        string password_hash
    }
    PROFILE {
        int id PK
        int user_id FK
        string fitness_goal
        string available_days
        string preferences
    }
    WORKOUT {
        int id PK
        int user_id FK
        string activity
        date workout_date
        int duration_minutes
    }
    MEAL {
        int id PK
        int user_id FK
        string description
        date meal_date
    }
    WEEKLY_PLAN {
        int id PK
        int user_id FK
        date week_start
        string status
        boolean ai_generated
    }
    PLAN_ITEM {
        int id PK
        int weekly_plan_id FK
        string day
        string activity
        int duration_minutes
    }
```

This is a first draft of the data model. Review the fields with your team and instructor before implementation. Do not store real health information in test data.
