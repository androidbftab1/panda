
from panda import Panda
panda = Panda()
#panda.can_recv()
panda.can_send(0x1aa, "message", 0)
