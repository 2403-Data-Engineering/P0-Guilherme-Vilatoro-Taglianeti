from dataclasses import dataclass


@dataclass
class ProfessorModel:
    id: int
    first_name: str
    last_name: str
    department: str
    email: str
    active = True