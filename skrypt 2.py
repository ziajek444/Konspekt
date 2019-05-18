# 1 Edycja zmiennych tekstowych

zmienna01 = 50
zmienna02 = 'A'
zmienna03 = chr(zmienna01)
zmienna04 = ord(zmienna02)
finish = " w tabeli ASCII\n"
print(str(zmienna01)+": "+zmienna03,zmienna02+": "+str(zmienna04),sep=finish,end=finish)

zmienna05 = 'któtki tekst między apostrofami'
zmienna06 = "któtki tekst między cudzysłowami"
zmienna07 = '''Bardzo długi tekst,
w którym dozwolone są znaki końca linii,
bez błędu kompilacji.
'''

print(zmienna05,zmienna06,zmienna07,sep="\n------------------------------\n")

commands =  ['strip()','capitalize()','count()','find()','istitle()','len()','join()','upper()']
commands += ['replace()','split()','title()','lower()']
zmienna08 = '''      __tekst__      '''
print(commands[0],"'"+zmienna08+"'","'"+zmienna08.strip()+"'",sep=" -> ")
zmienna08 = '''abc'''
print(commands[1],"'"+zmienna08+"'","'"+zmienna08.capitalize()+"'",sep=" -> ")
zmienna08 = '''Ala ma kota, ale altanka altruista'''
print(commands[2],"'"+zmienna08+"'",str(zmienna08.count("al"))+"x'al'",sep=" -> ")
print(commands[3],"'"+zmienna08+"'",str(zmienna08.find("al"))+" index",sep=" -> ")
zmienna08 = '''Book Real Title'''
print(commands[4],"'"+zmienna08+"'",str(zmienna08.istitle()),sep=" -> ")
zmienna08 = zmienna08.lower()
print(commands[4],"'"+zmienna08+"'",str(zmienna08.istitle()),sep=" -> ")
print(commands[5],"'"+zmienna08+"'",str(len(zmienna08)),sep=" -> ")
print(commands[6],"'"+zmienna08+"'","+".join(zmienna08),sep=" -> ")
print(commands[7],"'"+zmienna08+"'",zmienna08.upper(),sep=" -> ")
zmienna08 = '''Ala ma kota'''
print(commands[8],"'"+zmienna08+"'",zmienna08.replace("kota","małą myszkę"),sep=" -> ")
print(commands[9],"'"+zmienna08+"'",zmienna08.split(),sep=" -> ")
zmienna08 = '''Za DuŻo DużyCh ZnAkÓw...Za MaŁo MaŁyCH'''
print(commands[10],"'"+zmienna08+"'",zmienna08.title(),sep=" -> ")
print(commands[11],"'"+zmienna08+"'",zmienna08.lower(),sep=" -> ")

# ----------------------------
# 2 Usuwanie i podmiana stringów

zmienna09 = "inicjalizacyjny napis"

print(zmienna09,"ID obiektu: ",id(zmienna09))
zmienna09 = "nowystring"
print(zmienna09,"ID obiektu: ",id(zmienna09))
del zmienna09
# użycie zmiennej zmienna09 jest nie legalne po usunięciu, dlatego kod niżej wywoła błąd.
#print(zmienna09,"ID obiektu: ",id(zmienna09))

# ----------------------------
# 3 Sekwencje specjalne

zmienna10 = "standardowy tekst"
print(zmienna10)
zmienna10 = "\\ \\ \\ \"standardowy\t tekst\"\n\x49\x50\x51 \'\t\'"
print(zmienna10)
zmienna10 = r"\\ \\ \\ \"standardowy\t tekst\"\n\x49\x50\x51\n"
print(zmienna10)

# ----------------------------
# 3 Sekwencje specjalne

# Standardowy porządek 
zmienna11 = "{} {} {} {}".format('Python', 'Obsluga', 'Danych', 'Tekstowych') 
print("String wyświetlany normalnie:",zmienna11,sep="\n")
# Edycja pozycji
String1 = "{2} {3} {0} {1}".format('Python', 'Obsluga', 'Danych', 'Tekstowych')
print("String wyświetlany w innej kolejności:",zmienna11,sep="\n")
# Formatowanie liczb całkowitych
zmienna11 = "{0:b}".format(16)
print("Liczba całkowita biniarnie:",zmienna11,sep="\n")
# Formatowanie liczb zmiennoprzecinkowych 
zmienna11 = "{0:e}".format(165.6458) 
print("Liczba 165.6458 zmiennoprzecinkowa:",zmienna11,sep="\n")
# Zaokrąglanie liczb
zmienna11 = "{0:.2f}".format(1/6)
print("Liczba 1/6 zaokrąglona:",zmienna11,sep="\n")
# Justowanie i wyrównywanie tekstu
zmienna11 = "|{:<12}|{:^10}|{:^10}|{:>12}|".format('Python', 'Obsluga', 'Danych', 'Tekstowych') 
print("Wyrównany tekst:",zmienna11,sep="\n")


# ----------------------------



