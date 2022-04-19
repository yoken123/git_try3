import uuid
from Domain.utils.DataGateway import DataGateway
import os

class Classwork:
  def __init__(self, title, description, instruction_file, class_name):
    self.__id = str(uuid.uuid4())[:5]
    self.__title = title
    self.__description = description
    self.__instruction_file = instruction_file.filename
    self.__info = {}
    try:
      DataGateway.save_classwork(self.__id, self)
      instruction_file.save(os.path.join(DataGateway.get_classwork_path(self.__id), instruction_file.filename))
      classroom = DataGateway.get_data('Classroom', class_name)
      classroom.add_classwork(self.__id)
      DataGateway.save_data('Classroom', class_name, classroom)
    except:
      raise ValueError("Error!")

  def get_id(self):
    return self.__id
  
  def get_title(self):
    return self.__title
  
  def get_description(self):
    return self.__description
  
  def get_instruction_file(self):
    return self.__instruction_file

  def get_student_info(self, student_email):
    if student_email in self.__info:
      return self.__info[student_email]
      
  def get_student_grade(self, student_email):
    if student_email in self.__info:
      return self.__info[student_email]['grade']
  
  def get_student_file(self, student_email):
    if student_email in self.__info:
      print(self.__info[student_email]['file'])
      return self.__info[student_email]['file']

  def submit_student_work(self, student_email, file_name):
    if not student_email in self.__info:
      self.__info[student_email] = {
        'file': file_name,
        'grade': 0
      }
    self.__info[student_email]['file'] = file_name
    DataGateway.save_classwork(self.__id, self)
  
  def give_grade(self, student_email, grade):
    if student_email in self.__info:
      self.__info[student_email]['grade'] = grade
      DataGateway.save_classwork(self.__id, self)
  
  def get_info(self):
    return self.__info
  