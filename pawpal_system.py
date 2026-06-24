from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, time
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
        pass

    def get_datetime(self):
        """Combine due date and due time into one datetime value."""
        pass

    def is_recurring(self) -> bool:
        """Return whether the task repeats on a schedule."""
        pass


@dataclass
class Pet:
    """Represents a pet and its care tasks."""
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task for this pet."""
        pass

    def list_tasks(self) -> List[Task]:
        """Return the list of tasks for this pet."""
        pass


class Owner:
    """Represents the pet owner and their pets."""
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet for the owner."""
        pass

    def list_pets(self) -> List[Pet]:
        """Return the owner's pets."""
        pass

    def get_all_tasks(self) -> List[Task]:
        """Collect all tasks across the owner's pets."""
        pass


class Scheduler:
    """Schedules tasks for the owner's pets."""
    def __init__(self, owner: Owner) -> None:
        self.owner: Owner = owner

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks available for scheduling."""
        pass

    def sort_tasks_by_time(self) -> List[Task]:
        """Sort tasks by due time."""
        pass

    def filter_tasks_by_status(self, completed: bool) -> List[Task]:
        """Filter tasks by completion status."""
        pass

    def filter_tasks_by_pet(self, pet: Pet) -> List[Task]:
        """Filter tasks for a specific pet."""
        pass

    def detect_conflicts(self) -> List[Task]:
        """Detect conflicting tasks in the schedule."""
        pass

    def build_daily_schedule(self) -> List[Task]:
        """Build a sorted daily schedule across all pets."""
        pass
