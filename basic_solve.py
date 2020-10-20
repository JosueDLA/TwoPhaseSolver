import solver as sv
from threading import Thread
import start_server

# cube definition string of cube we want to solve
# See module enums.py for the format of the cube definition string
cubestring = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'

# Advantage: No network layer needed.
# Disadvantage: Only local usage possible.                                                                  #


# solve with a maximum of 20 moves and a timeout of 2 seconds for example
solve = sv.solve(cubestring, 20, 2)
print(solve)
quit()
