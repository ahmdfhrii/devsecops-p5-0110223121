from dataclasses import dataclass, asdict

@dataclass
class Task:
    id: int
    title: str
    done: bool = False

    def to_dict(self):
        return asdict(self)