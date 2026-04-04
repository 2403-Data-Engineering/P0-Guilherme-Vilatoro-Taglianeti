from sqlalchemy import String
from sqlalchemy.orm import  Mapped, mapped_column
from model.Base import Base


class ProfessorModel(Base):
    __tablename__= "professor"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    department: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(30), nullable=False)
    active: Mapped[bool] = mapped_column(default=True)

   


    def __repr__(self):
        return (
            "=====================================================\n"
            f"| {self.id} | {self.first_name} | {self.last_name} | "
            f"{self.department} | {self.email} | {self.active} |\n"
        )
