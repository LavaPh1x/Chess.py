class Rook:
  def __init__(self, color, position):
    self.position = position
    self.color = color

  def __str___(self):
    ...

  @classmethod
  def type(cls):
    return 'rook'



class Knight:
  def __init__(self, color, position):
    self.type = 'knight'
    self.position = position
    self.color = color

  def __str___(self):
    ...

  @classmethod
  def type(cls):
    return 'knight'


class Bishop:
  def __init__(self, color, position):
    self.type = 'bishop'
    self.position = position
    self.color = color

  def __str___(self):
    ...

  @classmethod
  def type(cls):
    return 'bishop'


class King:
  def __init__(self, color, position):
    self.type = 'king'
    self.position = position
    self.color = color
    self.castling_potential = True

  def __str___(self):
    ...

  @classmethod
  def type(cls):
    return 'king'


class Queen:
  def __init__(self, color, position):
    self.type = 'queen'
    self.position = position
    self.color = color

  def __str___(self):
    ...

  @classmethod
  def type(cls):
    return 'queen'


class Pawn:
  def __init__(self, color, position):
    self.type = 'pawn'
    self.position = position
    self.color = color

  def __str___(self):
    ...


  @classmethod
  def type(cls):
    return 'pawn'
