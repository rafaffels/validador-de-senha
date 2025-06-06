senha = str(input("Insira a senha: "))
senha_correta = "123456"

if senha_correta == senha:
    print("Senha correta")
elif len(senha) <6:
    print("Esta faltando um numero")
else:
    print("Senha incorreta")        