from dataclasses import dataclass


@dataclass
class StudentModel:
    id: int
    first_name: str
    last_name: str
    major: str
    email: str
    year: str
    active = True