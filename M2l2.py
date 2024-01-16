import random

caratteri_password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


lunghezza_password = int(input("Inserisci la lunghezza desiderata della password: "))


password_generata = ""


for _ in range(lunghezza_password):
    carattere_scelto = random.choice(caratteri_password)
    password_generata += carattere_scelto


print("Password generata:", password_generata)

