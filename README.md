# PawPal+ (Module 2 Project)

PawPal+ is a pet care planning assistant that helps a pet owner organize daily care tasks for multiple pets. It solves the problem of keeping track of task timings, priorities, and overlaps so the owner can review a daily plan and spot scheduling conflicts.

## System Design

The project uses four main classes:

- `Owner`: Stores owner information and manages multiple `Pet` objects.
- `Pet`: Stores a pet's name, species, and its list of `Task` objects.
- `Task`: Represents a pet care activity with a description, due date, due time, duration, completion status, frequency, and priority.
- `Scheduler`: Collects tasks from the `Owner` and provides sorting, filtering, conflict detection, and daily schedule generation.

The Mermaid UML diagram for this design is located in `diagrams/uml_draft.mmd`.

## Scheduler Algorithms

- Sorting tasks by date and time using each task's `due_date` and `due_time`.
- Filtering tasks by completion status using the task's `completed` flag.
- Filtering tasks by pet by checking which tasks belong to a specific `Pet`.
- Detecting conflicts using `duration_minutes` to compare a task's end time to the next task's start time.
- Generating a daily schedule by returning all tasks sorted chronologically.

## Getting Started

### Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Run the demo

```bash
python main.py
```

### Run the Streamlit app

The repository includes a starter `app.py` UI, but the scheduling logic is not yet connected to the Streamlit interface.

```bash
streamlit run app.py
```

## Demo Walkthrough

The `main.py` demo script illustrates this workflow:

1. Create an `Owner` and two `Pet` objects.
2. Add multiple `Task` objects for each pet, including tasks added out of time order.
3. Use `Scheduler` to build a sorted daily schedule.
4. Print incomplete tasks.
5. Print conflict warnings for overlapping tasks.

## Sample CLI Output

```text
🐾 Today's Sorted Schedule

2026-06-23 07:30 (10m) - Feed breakfast [high] ⏳ (Whiskers)
2026-06-23 08:00 (30m) - Morning walk [high] ⏳ (Rover)
2026-06-23 08:15 (15m) - Give medication [high] ⏳ (Whiskers)
2026-06-23 18:00 (20m) - Evening play session [medium] ⏳ (Rover)

🔎 Incomplete Tasks

- Morning walk (Rover) at 08:00 for 30 min
- Evening play session (Rover) at 18:00 for 20 min
- Feed breakfast (Whiskers) at 07:30 for 10 min
- Give medication (Whiskers) at 08:15 for 15 min

⚠️ Conflict Warnings

- Morning walk (Rover) overlaps at 08:00 on 2026-06-23
- Give medication (Whiskers) overlaps at 08:15 on 2026-06-23
```

## Testing

The test file `tests/test_pawpal.py` checks key behaviors for the core classes:

- `Task.mark_complete()` toggles a task from incomplete to complete.
- `Pet.add_task()` increases the pet's task count.
- `Scheduler.sort_tasks_by_time()` returns tasks in chronological order.

Test coverage currently includes task completion, task management, and scheduler sorting behavior.

Run the tests with:

```bash
python -m pytest
```

Sample passing output:

```text
============================= 3 passed in 0.03s =============================
```

## Project Status

The current implementation includes the core data model and scheduler logic for `Owner`, `Pet`, `Task`, and `Scheduler`. The demo script shows sorted scheduling, incomplete task listing, and basic conflict detection.

Future improvements could include connecting the scheduler logic to the Streamlit UI, adding task editing and removal, and refining scheduling rules for task priority and daily availability.
