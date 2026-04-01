from dataclasses import dataclass


@dataclass
class ClassModel:
    id: int
    name : str
    active = True