nome = input("digite seu nome: ")
print("Fala!", nome)

idade = int(input("Agora me diga sua idade! "))

def pesquisa():
    if(idade > 20):
        print("Tá ficando velhão.", idade, "maduro ein!")
    else:
        print("uma idade consideravel idade", idade)

pesquisa()