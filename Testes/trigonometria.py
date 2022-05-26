def hipotenusa(cat0, catA):
    h = (cat0**2 + catA**2)**0.5
    return h

def seno(cat0, catA):
    h = hipotenusa(cat0, catA)
    seno = cat0/h
    return seno

def cosseno(cat0, catA):
    h = hipotenusa(cat0, catA)
    cosseno = catA / h
    return cosseno

def tangente(cat0, catA):
    h = hipotenusa(cat0, catA)
    tan = seno(cat0, catA) / cosseno(cat0, catA)
    return