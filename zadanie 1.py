# zadanie 1

zmienna01 = 0
z02 = "|{0}:{4}\t{1}:{5}\t{2}:{6}\t{3}:{7}\t|"

print("{:^40}".format("ASCII table"))
while zmienna01 < (256):
    print(z02.format(zmienna01,zmienna01+1,zmienna01+2,zmienna01+3,chr(zmienna01),chr(zmienna01+1),chr(zmienna01+2),chr(zmienna01+3)))
    zmienna01 += 4


# ----------------------------



