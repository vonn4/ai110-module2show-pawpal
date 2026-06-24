from datetime import date, time

from pawpal_system import Owner, Pet, Scheduler, Task


def format_task(task: Task, pet_name: str) -> str:
    status = "✅" if task.completed else "⏳"
    return (
        f"{task.due_date} {task.due_time.strftime('%H:%M')} "
        f"({task.duration_minutes}m) - {task.description} [{task.priority}] {status} "
        f"({pet_name})"
    )


def get_pet_name_for_task(owner: Owner, task: Task) -> str:
    """Find the pet that owns the given task."""
    for pet in owner.list_pets():
        if task in pet.list_tasks():
            return pet.name
    return "Unknown"


def main() -> None:
    owner = Owner("Alex")

    rover = Pet(name="Rover", species="Dog")
    whiskers = Pet(name="Whiskers", species="Cat")

    owner.add_pet(rover)
    owner.add_pet(whiskers)

    rover.add_task(Task(
        description="Morning walk",
        due_date=date.today(),
        due_time=time(hour=8, minute=0),
        duration_minutes=30,
        priority="high",
    ))
    rover.add_task(Task(
        description="Evening play session",
        due_date=date.today(),
        due_time=time(hour=18, minute=0),
        duration_minutes=20,
        priority="medium",
    ))
    whiskers.add_task(Task(
        description="Feed breakfast",
        due_date=date.today(),
        due_time=time(hour=7, minute=30),
        duration_minutes=10,
        priority="high",
    ))
    whiskers.add_task(Task(
        description="Give medication",
        due_date=date.today(),
        due_time=time(hour=8, minute=15),
        duration_minutes=15,
        priority="high",
    ))

    scheduler = Scheduler(owner)

    print("\n🐾 Today's Sorted Schedule\n")
    schedule = scheduler.build_daily_schedule()
    for task in schedule:
        pet_name = get_pet_name_for_task(owner, task)
        print(format_task(task, pet_name))

    incomplete_tasks = scheduler.filter_tasks_by_status(completed=False)
    print("\n🔎 Incomplete Tasks\n")
    for task in incomplete_tasks:
        pet_name = get_pet_name_for_task(owner, task)
        print(f"- {task.description} ({pet_name}) at {task.due_time.strftime('%H:%M')} for {task.duration_minutes} min")

    conflicts = scheduler.detect_conflicts()
    print("\n⚠️ Conflict Warnings\n")
    if conflicts:
        for task in conflicts:
            pet_name = get_pet_name_for_task(owner, task)
            print(f"- {task.description} ({pet_name}) overlaps at {task.due_time.strftime('%H:%M')} on {task.due_date}")
    else:
        print("No conflicts detected.")


if __name__ == "__main__":
    main()
