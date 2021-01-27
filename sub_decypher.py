import sys
import csv

if len(sys.argv) == 2 and  sys.argv[1] == "-help":
	print("Usage ./decypher.py cipher.txt keys.csv")
	sys.exit(1)
if len(sys.argv) != 3:
	print(" Use ./decypher.py -help for help")
	sys.exit(2)

# Intitialisation
cipher = []
keyfile = []
# Reading cipher text

with open(sys.argv[1],"r") as cipher_file:
    cipher.append(cipher_file.read())

# Reading key
with open(sys.argv[2],"r") as key_file:
    kfile = csv.reader(key_file)
    for row in kfile :
        keyfile.append(row)
# spliting a string into a list of char
def split(file):
    arr = []
    for char in file:
        arr.append(char)
    return arr

decypher = []
cipher = cipher[0]
cipher.lower()

# decyphering according to provided key list
for index in keyfile:
    index = index[0]
    strippedkey = split(index)
    decyph = ''
    for char in cipher:
        if ord(char) >= 97 and ord(char) <= 122: 
            count = ord(char) - 97
            decyph += strippedkey[count]
        else:
            decyph += char
    decypher.append(decyph)

# Printing list of decypher text obtained
for decy in decypher:
    print(decy)

