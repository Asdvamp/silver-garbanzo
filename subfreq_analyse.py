import sys
import csv

if len(sys.argv) == 2 and  sys.argv[1] == "-help":
        print("Usage ./subfreq_analyse.py cipher.txt Y(if want to see key else N)")
        sys.exit(1)
if len(sys.argv) != 3:
        print(" Use ./subfreq_analyse.py -help for help")
        sys.exit(2)

# Intitialisation
cipher = []
keyfile = []
# Reading cipher text

with open(sys.argv[1],"r") as cipher_file:
    cipher.append(cipher_file.read())

cipher = cipher[0]
cipher.lower()

count = [0] * 26
keyfile = [0] * 26

# Intialising keyfile

for index in range(26):
    keyfile[index] = chr(97 + index)

# Counting no of times a 'char' appeared in cipher text

for char in cipher:
    if ord(char) >= 97 and ord(char) <= 122:
        count[ord(char) - 97] += 1
print("------------------------------------------------------------Cipher text provided --------------------------------------------------------------")
print("\n")
print(cipher)

print("------------------------------------------------------Frequency of 'char' in cipher text ------------------------------------------------------")

for index in range(26):
    print(chr(97 + index) +  " : " + str(count[index]) , end = " , ")
print("\n")

tick = 1

print("-----------------------------------------------------------------------------------------------------------------------------------------------")

while True:
    continuity = input("Want to continue decoding [y/n] : ")
    if continuity == 'n':
        break
    print(f"----------------------------------------------------------Decode count:  {tick}---------------------------------------------------------------------")
    replace = input("Char you want to replace : ")
    tochar = input("To the char : ")
    keyfile[ord(replace) - 97] = tochar
    # Storing modified text
    modif_ciph = ''
    for char in cipher:
        if char == replace:
            modif_ciph += tochar
        else:
            modif_ciph += char
    tick += 1
    print("\n")
    print(modif_ciph) 


if sys.argv[2] == 'Y':
    print("----------------------------------------------------------Decypher key ------------------------------------------------------------------------" )
    print(''.join(keyfile))

print("----------------------------------------------------------Decypher Text ------------------------------------------------------------------------" )

print(modif_ciph)
