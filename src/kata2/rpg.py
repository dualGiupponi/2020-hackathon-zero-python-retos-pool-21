#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    resultado = ""
    random.seed()
    for i in range(0,passLen):
        resultado += chr(random.randint(33, 126))

    return resultado
