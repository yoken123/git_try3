from Classes.Account.User import User
from func.Idgenerator import Idgenerator

class Student(User):
  def __init__(self, first_name, last_name, password, email):
      super().__init__(first_name = first_name, last_name = last_name, password = password, email = email, role="student", id = Idgenerator.generate_studentid())