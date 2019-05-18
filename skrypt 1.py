# 1 Podstawowe operacje tekstu

# zmienna typu string
zmienna1 = "111"
# zmienna typu int
zmienna2 = 222
# zmienna typu float
zmienna3 = 3.3
# zmienna typu lista
zmienna4 = ["lista", 4, 5.5]

print(zmienna1,    zmienna2,     zmienna3,     zmienna4, "444",sep=" + ",end=" $$ \n")
print(zmienna1,str(zmienna2),str(zmienna3),str(zmienna4),"444",sep=" + ",end=" $$ \n")

zmienna5 = int(zmienna1) + zmienna2

print("string plus int:",zmienna5,sep="\n")

# ----------------------------
# 2 Specjalne operatory stringów
print(end="\n\n")

zmienna6 = "Hello "
print("operator +",zmienna6 + "world",                                            sep=" : ",end=" $$ \n")
print("operator *",zmienna6 * 3,                                                  sep=" : ",end=" $$ \n")
print("operator []",zmienna6[0],                                                  sep=" : ",end=" $$ \n")
print("operator []",zmienna6[-1],                                                 sep=" : ",end=" $$ \n")
print("operator [:]",zmienna6[1:-2],                                              sep=" : ",end=" $$ \n")
print("operator in","e" in zmienna6,                                              sep=" : ",end=" $$ \n")
print("operator not in","k" not in zmienna6,                                      sep=" : ",end=" $$ \n")
print("operator r",r"\n\t",                                                       sep=" : ",end=" $$ \n")
print("operator %"," slowo %s, liczba %d, float %f" %(zmienna6,13,2.14),          sep=" : ",end=" $$ \n")

zmienna7 = "1024 + 1024"
zmienna8 = "1024"
zmienna9 =  eval(zmienna7)
zmienna10 = eval("1024 * 2")
zmienna11 = eval(zmienna8 + " / " + "4")
print("zmienne 9,10,11 są nie jawnie kastowane do stringa")
print(zmienna9,zmienna10,zmienna11,sep="\n")

print("dodawanie: "+str(zmienna9),"mnożenie: "+str(zmienna10),"dzielenie: "+str(zmienna11),sep="\n")

# zaawansowane używanie funkcji eval()
from math import *
M = "000000"
# liczba dużo większa niż możemy zapisać w systemie 64 bitowym
zmienna12 = "200"+M+M+M+M+M
print("wyniki dla wyrażenia:\nsqrt(("+zmienna12+"*99999999199999999)/1234567890987654321)\n")
print(eval("sqrt(("+zmienna12+"*99999999199999999)/1234567890987654321)",{"sqrt" : sqrt}))
print(sqrt((int(zmienna12)*99999999199999999)/1234567890987654321))

















