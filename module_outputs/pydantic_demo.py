from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name : str = 'Shivanshu' # default value
    age: Optional[int] = None # optional attribute
    email: EmailStr # built in data type in pydantic to validate email
    cgpa: float = Field(gt=0, lt=10, default=0, description= 'Decimal value representing the CGPA of the student') # field is used to apply constraints to a data column

new_student = {'age': 32, 'email':'st955218@gmail.com'}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict.get('age'))
print(student_dict.get('name'))
print(student_dict.get('city'))

