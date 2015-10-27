# from Flask Web Development chapter 8 page 94
class User:
  def get_id(self):
    return self.uid
  def __init__(self, uid):
    self.uid = uid
    self.is_authenticated = True
    self.is_active = True
    self.is_anonymous = False
