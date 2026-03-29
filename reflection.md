# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

Core actions a user should be able to perform (3):
- Track pets in household (multiple pet care plans)
- See todo or task list of the day for each pet (has priority set by user)
- Have a scheduling feature

Owner — stores the person's name, free time, and their list of pets. It's the top-level object everything else connects to.

Pet — stores a single animal's info and its list of care tasks. Can sort tasks by priority and sum up their total time.

CareTask — one thing that needs to get done. Holds the title, duration, and priority. Gets a scheduled_time assigned by the Scheduler later.

Scheduler — the logic class. Takes the Owner (and through it, all pets and tasks), builds a daily plan based on priority and available time, and can explain why tasks were chosen or skipped.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
1. PRIORITY_RANK dictionary — was added at the top so get_tasks_by_priority() sorts by number rank, not alphabetically
2. priority validation in CareTask.__init__ — would have raised a ValueError immediately if an invalid value is passed, catching typos early
3. set_scheduled_time() on CareTask — gives the Scheduler a clean method to assign a time instead of directly mutating task.scheduled_time from outside the class
4. Guards in generate_plan() — comments marking where to reset self.schedule before rebuilding and where to exit early if owner.pets is empty

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

classDiagram
    class Owner {
        +String name
        +int available_minutes
        +List~Pet~ pets
        +Dict preferences
        +add_pet(pet: Pet)
        +get_daily_availability() int
    }

    class Pet {
        +String name
        +String species
        +int age
        +List~CareTask~ tasks
        +add_task(task: CareTask)
        +get_tasks_by_priority() List~CareTask~
        +get_total_task_time() int
    }

    class CareTask {
        +String title
        +int duration_minutes
        +String priority
        +String scheduled_time
        +bool is_completed
        +mark_complete()
        +to_dict() Dict
    }

    class Scheduler {
        +Owner owner
        +List schedule
        +int total_time_used
        +generate_plan()
        +get_schedule() List
        +explain_plan() String
    }

    Owner "1" --> "1..*" Pet : owns
    Pet "1" --> "0..*" CareTask : has
    Scheduler "1" --> "1" Owner : reads from
    Scheduler "1" --> "1..*" Pet : schedules for

