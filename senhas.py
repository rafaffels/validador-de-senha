senha = str(input("Insira a senha: "))# aqui toda as letras colocadas serao identificadas como string
senha_correta = "123456" #nesta variavel se encontra a linha correta ("esta identificada como string")

if senha_correta == senha:# Compara se a senha digitada (senha) é igual à senha correta (senha_correta).
    print("Senha correta")
elif len(senha) <6: #Aqui, ele verifica se a quantidade de caracteres da senha digitada é menor que 6. len(senha) conta o número de caracteres da senha.
    print("Esta faltando um numero")#Se a senha não for correta e não for menor que 6 caracteres, essa é a opção final.
else:
    print("Senha incorreta")        