from Classes.Account.User import User
from func.Idgenerator import Idgenerator

class Professor(User):
  def __init__(self, frirst_name, last_name, password, email):
    super().__init__(id=Idgenerator.generate_professorid(), first_name=frirst_name, last_name=last_name, password=password, email=email, role="professor")