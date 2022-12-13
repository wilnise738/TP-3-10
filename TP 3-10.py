#Fonksyon ki jenere yon kod aleatwa a n karakte alfabetik san repetisyon
import string
import random
from random import *

def kòd_aleyatwa_alfabetik():
    alfabè=string.ascii_letters
    mo=randint(2, 61)

    kòd_aleatwa=""
    for i in range(mo):
        lèt=randint(0, 25)
        if alfabè[lèt] in kòd_aleatwa:
            lèt=randint(0, 25)
        else:
            kòd_aleatwa = kòd_aleatwa + alfabè[lèt]

    print(kòd_aleatwa)

#Fonksyon ki jenere yon kod aleatwa a n karakte alfanimerik san repetisyon
def kòd_aleyatwa_alfanimerik():
    alfabè=string.ascii_letters
    nimerik=string.digits

    mo2=randint(3, 61)
    alfanimerk=alfabè + nimerik

    kòd_aleatwa=""
    for i in range(mo2):
        lèt=randint(0, 61)
        if alfanimerk[lèt] in kòd_aleatwa:
            lèt=randint(0, 61)
        else:
            kòd_aleatwa = kòd_aleatwa + alfanimerk[lèt]

    print(kòd_aleatwa)
    
#Fonksyon ki jenere yon SLUG apati de yon chenn
def slug(mo):
    fraz= str(mo).split()
    print('-'.join(fraz))

mo=input("Antre yon fraz: \n")
print("Slug la se: ") 
slug(mo)

#Fonksyon ki separe 
def separe_mo(mo):
    return','.join(list(mo))

print(separe_mo('Meus'))

#Fonksyon ki kripte yon mo ak endeks li
import string
def endis_mo(mo):
    endis=[]
    for i in mo:
        endis.append(str(string.ascii_letters.index(i)))
    print("-".join(endis))
mo=input("Antre yon mo: \n")
print("Endis mo a se:")
endis_mo(mo)


#Fonksyon ki dekripte yon mo
import string
alfabe=string.ascii_letters

def mo_dekripte(endex):
    mo=[]
    for i in endex.split("-"):
        mo.append(alfabe[int(i)])
    print("".join(mo))

endex=input("Antre mo kripte a: \n")
print("Mo dekripte a se:")
mo_dekripte(endex)

# Foksyon ki pemite de vale
def pemite_vale(val1, val2):
    tanp=()
    tanp= val1, val2
    print(tanp[::-1])
val1=input("Antre yon vale: \n")
val2=input("Antre yon llt vale:\n")
print("Pemitasyon an se:")
pemite_vale(val1, val2)

#Fonksyonki retounen inisyal yon non
def retounen_inisyal(non):
    non_konple=[]
    inisyal=""
    for i in non:
        non=non.replace(" ","-")
    for i in non:
        non_konple.append(i)
    for i in non_konple:
        inisyal = inisyal + i[0]
    print(inisyal)

non=input("Ekri non an:\n")
print("Inisyal la se:\n")
retounen_inisyal(non)