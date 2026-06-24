from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, time, datetime, timedelta
from typing import List


@dataclass
class Task:
    """Represents a single pet care task."""
    description: str
    due_date: date
    due_time: time
    duration_minutes: int = 30
    completed: bool = False
    frequency: str = "none"
    priority: str = "medium"

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    def get_datetime(self) -> datetime:
        """Combine due date and due time into one datetime value."""
        return datetime.combine(self.due_date, self.due_time)

    def is_recurring(self) -> bool:
        """Return whether the task repeats on a schedule."""
        return bool(self.frequency and self.frequency.lower() != "none")


@dataclass
class Pet:
    """Represents a pet and its care tasks."""
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task for this pet."""
        self.tasks.append(task)

    def list_tasks(self) -> List[Task]:
        """Return the list of tasks for this pet."""
        return self.tasks


class Owner:
    """Represents the pet owner and their pets."""
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet for the owner."""
        self.pets.append(pet)

    def list_pets(self) -> List[Pet]:
        """Return the owner's pets."""
        return self.pets

    def get_all_tasks(self) -> List[Task]:
        """Collect all tasks across the owner's pets."""
        all_tasks: List[Task] = []
        for pet in self.pets:
            all_tasks.extend(pet.list_tasks())
        return all_tasks


class Scheduler:
    """Schedules tasks for the owner's pets."""
    def __init__(self, owner: Owner) -> None:
        self.owner: Owner = owner

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks available for scheduling."""
        return self.owner.get_all_tasks()

    def sort_tasks_by_time(self) -> List[Task]:
        """Sort tasks by due date and time."""
        return sorted(self.get_all_tasks(), key=lambda task: task.get_datetime())

    def filter_tasks_by_status(self, completed: bool) -> List[Task]:
        """Filter tasks by completion status."""
        return [task for task in self.get_all_tasks() if task.completed == completed]

    def filter_tasks_by_pet(self, pet: Pet) -> List[Task]:
        """Filter tasks for a specific pet."""
        return pet.list_tasks()

    def detect_conflicts(self) -> List[Task]:
        """Detect conflicting tasks in the schedule."""
        tasks = self.sort_tasks_by_time()
        conflicting_tasks: List[Task] = []
        for index in range(len(tasks) - 1):
            current = tasks[index]
            next_task = tasks[index + 1]
            current_end = current.get_datetime() + timedelta(minutes=current.duration_minutes)
            next_start = next_task.get_datetime()
            if current_end > next_start and current.get_datetime().date() == next_start.date():
                if current not in conflicting_tasks:
                    conflicting_tasks.append(current)
                if next_task not in conflicting_tasks:
                    conflicting_tasks.append(next_task)
        return conflicting_tasks

    def build_daily_schedule(self) -> List[Task]:
        """Build a sorted daily schedule across all pets."""
        return self.sort_tasks_by_time()
