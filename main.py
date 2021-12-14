import sounddevice as sd
import numpy as np

duration = -1  # seconds

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    print(f"Volume is now {int(volume_norm)}db",end="\r")

with sd.Stream(callback=print_sound):
    sd.sleep(duration * 1000)
