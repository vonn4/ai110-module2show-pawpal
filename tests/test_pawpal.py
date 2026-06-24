from datetime import date, time

from pawpal_system import Owner, Pet, Scheduler, Task


def test_task_mark_complete_changes_status() -> None:
    task = Task(
        description="Feed breakfast",
        due_date=date.today(),
        due_time=time(hour=8, minute=0),
    )

    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_pet_add_task_increases_task_count() -> None:
    pet = Pet(name="Buddy", species="Dog")
    assert len(pet.tasks) == 0

    pet.add_task(Task(
        description="Walk",
        due_date=date.today(),
        due_time=time(hour=9, minute=0),
    ))

    assert len(pet.tasks) == 1


def test_scheduler_sort_tasks_by_time_returns_chronological_order() -> None:
    owner = Owner("Sami")
    pet = Pet(name="Luna", species="Cat")
    owner.add_pet(pet)
    pet.add_task(Task(
        description="Evening snack",
        due_date=date.today(),
        due_time=time(hour=18, minute=30),
    ))
    pet.add_task(Task(
        description="Morning feeding",
        due_date=date.today(),
        due_time=time(hour=7, minute=30),
    ))

    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_tasks_by_time()

    assert sorted_tasks[0].description == "Morning feeding"
    assert sorted_tasks[1].description == "Evening snack"
