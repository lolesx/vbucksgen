import random

caracteres = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

while True:
    fortnitecode = ''
    fortnitecode_1 = ''
    fortnitecode_2 = ''
    fortnitecode_3 = ''


    for i in range(4):
        fortnitecode = f"{fortnitecode}{random.choice(caracteres)}"
        fortnitecode_1 = f"{fortnitecode_1}{random.choice(caracteres)}"
        fortnitecode_2 = f"{fortnitecode_2}{random.choice(caracteres)}"
        fortnitecode_3 = f"{fortnitecode_3}{random.choice(caracteres)}"

   
    print(f"{fortnitecode}-{fortnitecode_1}-{fortnitecode_2}-{fortnitecode_3}")

    with open("code.txt", "a+") as fortfile:

        fortfile.write(f"{fortnitecode}-{fortnitecode_1}-{fortnitecode_2}-{fortnitecode_3}\n")

        fortfile.close()
