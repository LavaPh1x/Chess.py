class InvalidMoveError(Exception):
  pass
class PositionError(Exception):
  pass

##############################################################

class Position:
  __alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
  __digits = ['1', '2', '3', '4', '5', '6', '7', '8']

  def __init__(self, position):
    self.name = position
    self.position = self.name

  def __add__(self, other):
    if not isinstance(other, tuple):
      raise TypeError("Move must be a tuple of length 2") #When the move isn't a tuple
    elif len(other) != 2:
      raise ValueError("Move must be a tuple of length 2") #When the move is a tuple, but not length 2
    elif not other[0] in range(-7, 8) or not other[1] in range(-7, 8):
      raise InvalidMoveError("Move does not contain valid coordinates") #When the tuple elements aren't both digits between -7 and 7
    x = self.__alphabet.index(self.position[0]) + other[0]
    y = int(self.position[1]) + other[1]
    if not x in range(8) or not y in range(1,9):
      raise InvalidMoveError("Cannot move piece off the board") #When the new position would be off the board
    else: return self.__alphabet[x] + str(y)

  def __sub__(self, other):
    if not isinstance(other, Position):
      raise TypeError("Positions may only be subtracted from each other")
    x1 = self.__alphabet.index(self.position[0])
    y1 = int(self.position[1])
    x2 = other.__alphabet.index(other.position[0])
    y2 = int(other.position[1])
    return (x1 - x2, y1 - y2)

  def __str__(self):
    return self.position

  @property
  def position(self):
    return self._position

  @position.setter
  def position(self, pos):
    if isinstance(pos, str):
      if len(pos) == 2 and pos[0] in self.__alphabet and pos[1] in self.__digits:
        self._position = pos
      else: raise PositionError(f"'{self.name}' is an invalid position")
    else: raise PositionError(f"'{self.name}' is an invalid position")




###############################################################

class Piece:
  __alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
  __digits = ['1', '2', '3', '4', '5', '6', '7', '8']

  def __init__(self, color, position):
    self.position = position
    self.color = color

  def __str__(self):
    ...

  @property
  def position(self):
    return self._position

  @position.setter
  def position(self, pos):
    if isinstance(pos, str):
      if len(pos) == 2 and pos[0] in self.__alphabet and pos[1] in self.__digits:
        self._position = Position(pos)
      else: raise PositionError(f"A {self.type()} was assigned an invalid position")
    else: raise PositionError(f"A {self.type()} was assigned an invalid position")


  @property
  def color(self):
    return self._color

  @color.setter
  def color(self, col):
    if isinstance(col, str) and not hasattr(self, '_color'):
      if col == 'white' or col == 'black':
        self._color = col
      else: ...
    else: ...

###############################################################

class Rook(Piece):

  def __init__(self, color, position):
    super().__init__(color, position)

  def __str__(self):
    ...

  @classmethod
  def type(cls):
    return 'rook'

###############################################################

class Knight(Piece):

  def __init__(self, color, position):
    super().__init__(color, position)

  def __str__(self):
    ...

  @classmethod
  def type(cls):
    return 'knight'

###############################################################

class Bishop(Piece):

  def __init__(self, color, position):
    super().__init__(color, position)

  def __str__(self):
    ...

  @classmethod
  def type(cls):
    return 'bishop'

###############################################################

class King(Piece):

  def __init__(self, color, position):
    super().__init__(color, position)

  def __str__(self):
    ...

  @classmethod
  def type(cls):
    return 'king'

###############################################################

class Queen(Piece):

  def __init__(self, color, position):
    super().__init__(color, position)

  def __str__(self):
    ...

  @classmethod
  def type(cls):
    return 'queen'

###############################################################

class Pawn(Piece):

  def __init__(self, color, position):
    super().__init__(color, position)

  def __str__(self):
    ...

  @classmethod
  def type(cls):
    return 'pawn'

###############################################################
