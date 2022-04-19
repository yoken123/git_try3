from Domain.utils.DataGateway import DataGateway
import bcrypt
class Account:
  def __init__(self, id, first_name, last_name, password, email, role):
    if (DataGateway.is_data_existed('User', email)):
      raise ValueError('Unsuccessfully created! (there is an account link with the email address)')
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10)) # hashing with bcrypt data needs to be byte
    self.__id = id
    self.__first_name = first_name
    self.__last_name = last_name
    self.__password = password_hash
    self.__email = email
    self.__role = role
    DataGateway.save_data('User', self.__email, self)
  
  def get_id(self):
    return self.__id
  
  def get_name(self):
    return self.__first_name, self.__last_name

  def get_name_string(self):
    return self.__first_name + " " + self.__last_name
  
  def get_password(self):
    return self.__password
  
  def get_email(self):
    return self.__email
  
  def get_role(self):
    return self.__role

  def get_id(self):
    return self.__id
  
  def set_name(self, first_name, last_name):
    self.__first_name = first_name
    self.__last_name = last_name
  
  def set_password(self, password):
    self.__password = password
  
  def set_email(self, email):
    self.__email = email
  
  def set_role(self, role):
    self.__role = role
  
  def delete_account(self, email, password):
    if (not DataGateway.is_data_existed('User', email)):
      raise ValueError("Unsuccessfully deleted! (no account link with the email)")
    if (not self.verify_pw(password)):
      raise ValueError("Unsuccessfully deleted! (password entered is incorrect)")
    try:
      DataGateway.delete_data('User', self.get_email())
      return True
    except:
      print("Unsuccessfully deleted!")
      raise ValueError("Unsuccessfully deleted!")
  
  def verify_pw(self, enter_password):
    return bcrypt.checkpw(enter_password.encode('utf-8'), self.get_password())
  
  def get_data(self, email):
    try:
      return DataGateway.get_data('User', email)
    except:
      raise ValueError("There is no User corresponding to the email!")