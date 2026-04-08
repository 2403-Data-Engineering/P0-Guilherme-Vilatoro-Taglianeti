from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import  Mapped, mapped_column
from model.Base import Base


class StudentClass(Base):
    __tablename__= "StudentClass"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    class_id: Mapped[int] = mapped_column(ForeignKey("class.id"))
    student_id: Mapped[int] = mapped_column(ForeignKey("student.id"))
    active: Mapped[bool] = mapped_column(default=True)
    
    __table_args__ = (
        UniqueConstraint("class_id", "student_id", name="uq_class_student"),
    )