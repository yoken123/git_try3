from Domain.utils.DataGateway import DataGateway
import uuid

class Classroom:
  def __init__(self, name, description, max_student, creator, is_private, id=uuid.uuid4(), code=None):
    try:
      if (DataGateway.is_data_existed('Classroom', name)):
        raise ValueError('Unsuccessfully created! (there is classroom with that name)')
      if len(name) < 2:
        raise ValueError("Name must be longer than 2 characters!")
      elif len(description) < 3:
        raise ValueError("Description must be longer than 3 characters!")
      elif max_student < 0:
        raise ValueError("Max number of student must be larger than 0!")
    except ValueError as e:
      raise e
    self.__id = str(id)
    self.__name = name
    self.__description = description
    self.__max_student_number = max_student
    self.__student_list = {}
    self.__creator = creator.get_email()
    self.__classwork_list = []
    self.__announcements = []
    self.__is_private = is_private
    self.__code = code
    creator.enroll(name)
    DataGateway.save_data('User', creator.get_email(), creator)
    DataGateway.save_data("Classroom", self.__name, self)

  def get_id (self):
    return self.__id
  
  def set_id (self, id):
    self.__id = id
  
  def get_name(self):
    return self.__name
  
  def set_name(self, name):
    self.__name = name

  def get_description(self):
    return self.__description
  
  def set_description(self, description):
    self.__description = description
  
  def get_max_student_number(self):
    return self.__max_student_number
  
  def set_max_student_number(self, number):
    self.__max_student_number = number
  
  def get_student_list(self):
    return self.__student_list
  
  def set_student_list(self, list):
    self.__student_list = list
  
  def get_professor_lsit(self):
    return self.__professor_list
  
  def set_professor_list(self, list):
    self.__professor_list = list

  def get_creator(self):
    return self.__creator
  
  def set_creator(self, creator):
    self.__creator = creator
  
  def is_creator(self, email):
    return self.__creator == email

  def get_classwork(self):
    return self.__classwork_list
  
  def add_classwork(self, classwork):
    self.__classwork_list.append(classwork)

  def is_private(self):
    return self.__is_private
  
  def set_private(self, private):
    self.__is_private = private
  
  def add_student(self, student_email):
    self.__student_list[student_email] = { "score": 0 }
  
  def add_professor(self, professor_email):
    self.__professor_list.append(professor_email)
  
  def remove_student(self, student_email):
    del self.__student_list[student_email]
  
  def remove_professor(self, professor_email):
    if (professor_email == self.__creator):
      raise ValueError("The professor is the creator of the class!")
    self.__professor_list.remove(professor_email)
  
  def get_code(self):
    return self.__code
  
  def get_announcements(self):
    return self.__announcements
  
  def add_announcement(self, annoucement):
    self.__announcements.append(annoucement)
  
  def check_enrollment(self, student_email):
    if (student_email in self.__student_list):
      return True
    else:
      return False
  
  def join_classroom(classname, code, user):
    try:
      if DataGateway.is_data_existed('Classroom', classname):
        classroom = DataGateway.get_data('Classroom', classname)
        if user.get_email() in classroom.get_student_list() or classroom.is_creator(user.get_email()):
          raise ValueError('User is already in the classroom')

        if classroom.is_private():
          if not classroom.get_code() == code:
            raise ValueError('Code is not correct')
            
        classroom.add_student(user.get_email())

        user.enroll(classroom.get_name())
        DataGateway.save_data('User', user.get_email(), user)
        DataGateway.save_data('Classroom', classroom.get_name(), classroom)
      else:
        raise ValueError('Classroom is not exist!')

    except ValueError as e:
      raise e

  def get_student_grade(self, student_email):
    try:
      student_score = 0
      student_scores = []
      if len(self.__classwork_list) > 0:
        for classwork in self.__classwork_list:
          if DataGateway.get_classwork(classwork).get_student_grade(student_email):
            student_scores.append(DataGateway.get_classwork(classwork).get_student_grade(student_email))
        if len(student_scores) > 0:  
          for score in student_scores:
            student_score += score
        if student_score == 0:
          return student_score
        student_score /= (len(student_scores))
    except:
      raise ValueError('Error')
    return student_score