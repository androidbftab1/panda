#!/usr/bin/env python3
import os
import sys
import struct
import time

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from panda import Panda  # noqa: E402

if __name__ == "__main__":
  if os.getenv("WIFI") is not None:
    p = Panda("WIFI")
  else:
    p = Panda()
  print(p.get_serial())
  print(p.health())

  t1 = time.time()
  for i in range(100):
    p.get_serial()
  t2 = time.time()
  print("100 requests took %.2f ms" % ((t2 - t1) * 1000))

  p.set_safety_mode(Panda.SAFETY_ALLOUTPUT)
  print("Panda.SAFETY_ALLOUTPUT")

  a = 0
  if True:
    # flood
    msg_r = b"\x0a\x00\x00\x80\x00\x00\x00\x00"
    msg_m = b"\x00\x00\x00\x80\x00\x00\x00\x00"
    msg_p = b"\x00\x00\x00\x40\x00\x00\x00\x00"
    msg_n = b"\x0a\x00\x00\x00\x00\x00\x00\x00"
    #p.can_send(0x475, msg, 0)
    print("p.can_send 0x430 b'0a00000000000000'")
    p.can_send(0x430, msg_n, 0)
    time.sleep(0.2)
    p.can_send(0x430, msg_n, 0)
    time.sleep(0.2)
    p.can_send(0x430, msg_n, 0)
    time.sleep(0.2)
    p.can_send(0x430, msg_n, 0)
    time.sleep(0.2)
    p.can_send(0x430, msg_n, 0)
    time.sleep(0.2)

    dat = p.can_recv()
    if len(dat) > 0:
      print(dat)
    a += 1
