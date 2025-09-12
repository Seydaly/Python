import pytest
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from SQL_table import Student, engine


TestingSessionLocal = sessionmaker(bind=engine, expire_on_commit=False, future=True)

@pytest.fixture(scope="function")
def db_session():
    session = TestingSessionLocal()
    session.execute(text("TRUNCATE TABLE students RESTART IDENTITY CASCADE;"))
    session.commit()

    try:
        yield session
    finally:
        session.close()

def test_add_student(db_session):
    student = Student(user_id=1, level="beginner", education_form="group", subject_id=101)
    db_session.add(student)
    db_session.commit()

    db_student = db_session.get(Student, 1)
    assert db_student is not None
    assert db_student.level == "beginner"

def test_update_student_level(db_session):
    student = Student(user_id=2, level="beginner", education_form="personal", subject_id=102)
    db_session.add(student)
    db_session.commit()

    db_student = db_session.get(Student, 2)
    db_student.level = "intermediate"
    db_session.commit()

    updated_student = db_session.get(Student, 2)
    assert updated_student.level == "intermediate"

def test_delete_student(db_session):
    student = Student(user_id=3, level="intermediate", education_form="group", subject_id=103)
    db_session.add(student)
    db_session.commit()

    db_student = db_session.get(Student, 3)
    db_session.delete(db_student)
    db_session.commit()

    deleted_student = db_session.get(Student, 3)
    assert deleted_student is None
