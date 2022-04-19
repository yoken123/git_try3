from Classes.Classroom.Classroom import Classroom

class PrublicClassroom(Classroom):
  def __init__(self, name, description, max_number_student, creator_email):
    super().__init__(name, description, max_number_student, creator_email, is_private=False)
    