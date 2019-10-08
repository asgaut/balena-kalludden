# Stubs for RPi.GPIO module

from __future__ import print_function

BCM = 1
OUT = 1

def setmode(mode):
    return

def setwarnings(w):
    return

def setup(p, d):
    return

def output(p, v):
    print("Setting simulated relay output:", v)
