import time

def barra_de_carregamento():
    for _ in range(1):
        print("", end="", flush=True)
        time.sleep(0.9)

# Solicita dois números ao usuario
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Exibe "Calculando..."
print("Calculando...")
barra_de_carregamento()

# Realiza a soma
soma = numero1 + numero2

# Exibe o resultado
print(f"\n A soma de {numero1} e {numero2} são: {soma}")

from colorama import Fore

frase_vermelha = Fore.RED + "Obrigado por usar!" + Fore.RESET
print(frase_vermelha)
