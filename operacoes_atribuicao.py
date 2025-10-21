saldo = int(input("Digite o saldo inicial: "))

deposito = int(input("Digite o valor do depósito: "))

saldo += deposito  # saldo = saldo + deposito

print("Saldo após depósito:", saldo)

saque = int(input("Digite o valor do saque: "))

saldo -= saque  # saldo = saldo - saque

print("Saldo após saque:", saldo)

print("Saldo final:", saldo)

