from Classes.Account.Account import Account
from func.Idgenerator import Idgenerator

class Admin(Account):
  def __init__(self, first_name, last_name, password, email):
    super().__init__(id=Idgenerator.generate_adminid(), first_name=first_name, last_name=last_name, password=password, email=email, role="admin")