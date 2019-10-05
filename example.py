import os
from RingPy import Ring

r = Ring.Ring()
user = input("username: ")
password = input("password: ")
r.Authenticate(user, password)
r.EstablishSession()
r.GetDevices()

outputDir = "data"
if not os.path.exists(outputDir):
    os.mkdir(outputDir)

history = r.GetHistory()
for h in history:
    r.GetRecording(h["id"], outputDir)