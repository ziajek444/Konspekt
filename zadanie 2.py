# zadanie 2

with open("plik.txt") as file:
    dane = file.read()

zmienna01 = 0
licznik = []
while zmienna01 < 255:
    licznik += [dane.count(chr(zmienna01))]
    zmienna01 += 1
print(licznik)

zmienna01 = 0
z02 = "|{0}:{4}:[{8}]\t{1}:{5}:[{9}]\t{2}:{6}:[{10}]\t{3}:{7}:[{11}]\t|"

print("{:^40}".format("ASCII table"))
while zmienna01 < (256):
    print(z02.format(zmienna01,zmienna01+1,zmienna01+2,zmienna01+3,chr(zmienna01),chr(zmienna01+1),chr(zmienna01+2),chr(zmienna01+3),licznik[zmienna01],licznik[zmienna01+1],licznik[zmienna01+2],licznik[zmienna01+3]))
    zmienna01 += 4


# ----------------------------



