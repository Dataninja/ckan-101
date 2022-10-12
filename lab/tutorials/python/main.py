import sys
from random import randint

if len(sys.argv) > 1:
  print(f"Hello {sys.argv[1]}!")
else:
  for n in range(randint(1,10)):
    print(f"{n+1}. Hello world!")
