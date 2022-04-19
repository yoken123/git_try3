from Classes.Classroom.Classroom import Classroom
import uuid

class PrivateClassroom(Classroom):
  def __init__(self, name, description, max_number_student, creator_email):
    self.__code = (str(uuid.uuid4())[:5]).upper()
    super().__init__(name, description, max_number_student, creator_email, is_private=True, code=self.__code)
  
  def get_code(self):
    return self.__code
  
  def verify_code(self, code):
    return code == self.__code