
'''
Functions to improve the geometry features of tkinter.
'''

def sign(x):
  if x < 0:
    return -1
  else:
    return 1

def DrawLine(x1, y1, x2, y2, thickness, colour, canvas):
  if thickness != 0:
    for i in range(-thickness, thickness+1, sign(thickness)):
      canvas.create_line(x1, y1+i, x2, y2+i, fill=colour)