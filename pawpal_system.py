PRIORITY_RANK = {"high": 3, "medium": 2, "low": 1}


class Owner:
    def __init__(self, name: str, available_minutes: int, preferences: dict = None):
        self.name = name
        self.available_minutes = available_minutes
        self.pets: list["Pet"] = []
        self.preferences: dict = preferences or {}

    def add_pet(self, pet: "Pet"):
        pass

    def get_daily_availability(self) -> int:
        pass


class Pet:
    def __init__(self, name: str, species: str, age: int):
        self.name = name
        self.species = species
        self.age = age
        self.tasks: list["CareTask"] = []

    def add_task(self, task: "CareTask"):
        pass

    def get_tasks_by_priority(self) -> list["CareTask"]:
        # use PRIORITY_RANK to sort, not alphabetical string comparison
        pass

    def get_total_task_time(self) -> int:
        pass


class CareTask:
    def __init__(self, title: str, duration_minutes: int, priority: str):
        if priority not in PRIORITY_RANK:
            raise ValueError(f"priority must be 'high', 'medium', or 'low' — got '{priority}'")
        self.title = title
        self.duration_minutes = duration_minutes
        self.priority = priority
        self.scheduled_time: str | None = None
        self.is_completed: bool = False

    def set_scheduled_time(self, t: str):
        # called by Scheduler instead of mutating scheduled_time directly
        pass

    def mark_complete(self):
        pass

    def to_dict(self) -> dict:
        pass


class Scheduler:
    def __init__(self, owner: "Owner"):
        self.owner = owner
        self.schedule: list[tuple["Pet", "CareTask"]] = []
        self.total_time_used: int = 0

    def generate_plan(self):
        # guard: raise or return early if owner.pets is empty
        # reset self.schedule and self.total_time_used before building
        pass

    def get_schedule(self) -> list:
        # should only be called after generate_plan()
        pass

    def explain_plan(self) -> str:
        pass
