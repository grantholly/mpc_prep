#!/usr/bin/env python3
import os
import re
import sys
import wave
import subprocess


def get_sample_rate(f):
    with open(f, "rb") as wf:
        return wf.getsamplerate()

# check that we don't overwrite anything accidentally
FN = sys.argv[1]
print(os.path.isfile(FN))
print(f"preparing {FN}")
name, ext = os.path.splitext(FN)
name = re.sub(r"[^\w\s]", "", name)
name = [ s for s in name.split(" ") if s != "" ]
name = "_".join(name)

if len(name) > 16:
    fixed = (name[:16] + ext)
else:
    fixed = name + ext

print(f"creating {fixed} from {FN}")

cmd = f"ffmpeg -loglevel info -i \"{FN}\" -ar 44100 {fixed} -y"
print(f"running ffmpeg with {cmd}")
ret = subprocess.run(cmd, shell=True)
print(ret)
