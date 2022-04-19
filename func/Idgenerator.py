import json
import jsonpickle

class Idgenerator:
  '''
  This class will help generated a custom id
  '''
  def generate_id(key):
    with open("./func/id/id.json") as IDs:
      ids = json.load(IDs)
    last_id = ids[key]
    code = ""
    new_id = int(last_id) + 1
    for digit in range(0, 6 - len(str(new_id))):
      code += "0"
    code += str(new_id)
    ids[key] = code
    with open("./func/id/id.json", 'w') as IDs:
      json.dump(ids, IDs, indent=4)
    return code

  def generate_studentid():
    '''
    Generate student id started with code letter 'S'
    '''
    return "S" + Idgenerator.generate_id("student")
  
  def generate_professorid():
    """
    Generate professor id started with code letter 'P'
    """
    return "P" + Idgenerator.generate_id("professor")

  def generate_adminid():
    """
    Generate admin id started with code letter 'A'
    """
    return "A" + Idgenerator.generate_id("admin")