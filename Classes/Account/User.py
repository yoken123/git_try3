from Classes.Account.Account import Account

class User(Account):
  def __init__(self, id, first_name, last_name, password, email, role):
    self.__class_list = []
    super().__init__(id, first_name, last_name, password, email, role)
  
  def get_class_list(self):
    return self.__class_list
    
  def enroll(self, class_id):
    self.__class_list.append(class_id)
  
  def drop_class(self, class_id):
    if class_id in self.__class_list:
      self.__class_list.remove(class_id)
      return True
    else:
      print('No id corresponding to the class!')
      return False