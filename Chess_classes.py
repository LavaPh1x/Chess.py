class Rook:
  __alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  __digits = str(range(1, 9))

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
        self._position = pos
      else:...
    else: ...

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

  @classmethod
  def type(cls):
    return 'rook'

###############################################################

class Knight:
  __alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  __digits = str(range(1, 9))

  def __init__(self, color, position):
    self.type = 'knight'
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
        self._position = pos
      else:...
    else: ...

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

  @classmethod
  def type(cls):
    return 'knight'

###############################################################

class Bishop:
  __alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  __digits = str(range(1, 9))

  def __init__(self, color, position):
    self.type = 'bishop'
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
        self._position = pos
      else:...
    else: ...

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

  @classmethod
  def type(cls):
    return 'bishop'

###############################################################

class King:
  __alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  __digits = str(range(1, 9))

  def __init__(self, color, position):
    self.type = 'king'
    self.position = position
    self.color = color
    self.castling_potential = True

  def __str__(self):
    ...

  @property
  def position(self):
    return self._position

  @position.setter
  def position(self, pos):
    if isinstance(pos, str):
      if len(pos) == 2 and pos[0] in self.__alphabet and pos[1] in self.__digits:
        self._position = pos
      else:...
    else: ...

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

  @classmethod
  def type(cls):
    return 'king'

###############################################################

class Queen:

  __alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  __digits = str(range(1, 9))
  def __init__(self, color, position):
    self.type = 'queen'
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
        self._position = pos
      else:...
    else: ...

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

  @classmethod
  def type(cls):
    return 'queen'

###############################################################

class Pawn:
  __alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  __digits = str(range(1, 9))
  
  def __init__(self, color, position):
    self.type = 'pawn'
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
        self._position = pos
      else:...
    else: ...

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

  @classmethod
  def type(cls):
    return 'pawn'

###############################################################
