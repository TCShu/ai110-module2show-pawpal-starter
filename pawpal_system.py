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
        pass

    def get_total_task_time(self) -> int:
        pass


class CareTask:
    def __init__(self, title: str, duration_minutes: int, priority: str):
        self.title = title
        self.duration_minutes = duration_minutes
        self.priority = priority  # "low", "medium", or "high"
        self.scheduled_time: str | None = None
        self.is_completed: bool = False

    def mark_complete(self):
        pass

    def to_dict(self) -> dict:
        pass


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner
        self.schedule: list[tuple[Pet, CareTask]] = []
        self.total_time_used: int = 0

    def generate_plan(self):
        pass

    def get_schedule(self) -> list:
        pass

    def explain_plan(self) -> str:
        pass
