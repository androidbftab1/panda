#!/usr/bin/env python3
import os
import sys
import random
import time

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from panda import Panda  # noqa: E402

def get_test_string():
  return b"test" + os.urandom(10)

if __name__ == "__main__":
  p = Panda()
  p.set_safety_mode(Panda.SAFETY_ALLOUTPUT)

  print("Spamming all buses...")
  while True:
    #at = random.randint(1, 2000)
    at = 1141
    #st = get_test_string()[0:8]
    st = "0000008000000000"
    #bus = random.randint(0, 2)
    bus = 1
    p.can_send(at, st, bus)
    time.sleep(0.01)
    # print("Sent message on bus: ", bus)
