from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database model
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    salary = Column(Integer)

# Create an SQLite engine and session
engine = create_engine('sqlite:///example.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Function to get top 10 highest-paid employees
def get_top_paid_employees():
    # Query top 10 employees based on salary
    top_employees = session.query(Employee).order_by(Employee.salary.desc()).limit(10).all()

    # Print the result
    for emp in top_employees:
        print(f"ID: {emp.id}, Name: {emp.name}, Salary: {emp.salary}")

# Call the function to get top 10 employees
get_top_paid_employees()

# Close the session
session.close()
