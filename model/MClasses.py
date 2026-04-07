from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from model.Base import Base


class ClassModel(Base):
    __tablename__= "class"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    prof_id: Mapped[int] = mapped_column(ForeignKey("professor.id"))
    active: Mapped[bool] = mapped_column(default=True)

    def __repr__(self):
        return ("=====================================================\n"
            f"| {self.id} | {self.name} | {self.prof_id} |\n")