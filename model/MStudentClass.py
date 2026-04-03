from sqlalchemy import ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column
from model.Base import Base


class StudentClass(Base):
    __tablename__= "StudentClass"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    class_id: Mapped[int] = mapped_column(ForeignKey("class.id"))
    student_id: Mapped[int] = mapped_column(ForeignKey("student.id"))