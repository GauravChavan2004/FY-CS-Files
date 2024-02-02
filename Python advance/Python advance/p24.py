def KelvinToFahrenhit(temp):
    assert(temp>=0),"colder than absolute zero!"
    return((temp-273)*1.8)+32

print(KelvinToFahrenhit(273))
print(int(KelvinToFahrenhit(505.78)))
print(KelvinToFahrenhit(-10))
