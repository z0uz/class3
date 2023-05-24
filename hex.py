import hashlib

eingabe = "Unser Text für die Nutzung von SHA-256"

eingabe_codiert = eingabe.encode('utf-8')

hashwert = hashlib.sha256(eingabe_codiert)

hashwert_hex = hashwert.hexdigest()

print(f"SHA-256-HASH des textes: {hashwert_hex}")


#Or  u can use this short one liner code.

#import hashlib
#print(f"SHA-256 HASH des Textes: {hashlib.sha256('Unser Text für die Nutzung von SHA-256'.encode('utf-8')).hexdigest()}")
