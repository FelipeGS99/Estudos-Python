nome = str(input("Digite seu nome: ")).strip()
#Ambos prints funcionam, o primeiro foi a gambiarra que eu consegui fazer primeiro
#sabendo que se o .find() for falso ele retornará o valor -1
print(nome.upper().find("SILVA") >= 0)
print("SILVA" in nome.upper()) 