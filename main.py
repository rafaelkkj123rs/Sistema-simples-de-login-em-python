import time
import os 



def clear():
    os.system("cls")

clear()

print("Carregando sistema...")
time.sleep(2)
clear()

#CADASTRO
nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")
clear()

# LOGIN
nomeL = input("Digite seu nome: ")
senhaB = input("Digite sua senha: ")
clear()

if nome == nomeL and senha == senhaB:
    time.sleep(2)
    print("login com sucesso")
    time.sleep(4)
else:
    time.sleep(1)
    print("nome ou senha invalidos")
    time.sleep(5)

    

