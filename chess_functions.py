import re


def checkmove(chess_piece, destination):
    import re
    move = Position(destination.lower()) - chess_piece.position
    for Move in chess_piece.valid_moves:
        if re.search(Move, str(move)): return True
        else: continue
    return False
    
  
def updateboard(piece, position):
      if not checkmove: ...
  ...
