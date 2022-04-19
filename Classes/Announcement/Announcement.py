from Domain.utils.DataGateway import DataGateway
import uuid

class Announcement:
  def __init__(self, title, content, classroom, id=uuid.uuid4()):
    if (DataGateway.is_data_existed('Announcement', id)):
      raise ValueError("Already Existed!")
    self.__id = str(id)
    self.__title = title
    self.__content = content
    DataGateway.save_data('Announcement', self.__id, self)
    classroom.add_announcement(self.__id)
    DataGateway.save_data("Classroom", classroom.get_name(), classroom)

  def get_id(self):
    return self.__id
  
  def get_title(self):
    return self.__title
  
  def get_content(self):
    return self.__content