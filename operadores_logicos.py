saldo = 1000
saque = 200
limite = 500

if saque <= saldo and saque <= limite:
    saldo -= saque
    print("Saque realizado com sucesso!")
    print(f"Saldo restante: {saldo}")
else:
    print("Saque não autorizado. Verifique seu saldo e limite.")
    
    
        
saldo = 1000
saque = 250
limite = 200

conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque

print(True and True)


(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(True or False)

