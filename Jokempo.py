from funcao import bem_vindo, jogo

bem_vindo.boas_vinda()

#Função para escolher o modo de jogo (No momento só terá 2)
def modo_de_Jogo():

    print("Agora escolha o modo de jogo que queira jogar:\n[1] Modo Rápido (Uma rodada e acabou)\n[2] Modo Multiplas rodadas (Você joga um total de 5 rodadas)\n[3]Sair")
    print("Notas do Desenvolvedor: Mais para frente colocarei para escolher a quantidade de rodadas\n")

    while True:
        try:
            opcaoDeModo = int(input("Esolha o modo de Jogo que deseja \n-> "))
            
            if opcaoDeModo == 1:
                return 1
            
            elif opcaoDeModo == 2:
                return 2
            
            else:
                return 3
            
        except ValueError:
            print("Insira um valor inteiro\n")
    

def main():
    
    print('''Seja Bem-Vindo(a).
Aqui você irá jogar o famoso Jokempô, mais conhecido como Pedra, Papel, Tesoura.
Então relaxa e agachar, fique bem tranquilo aí e se divirta ;)\n''')
    
    while True:
        modo = modo_de_Jogo()
        if modo == 1:
            jogo.jogar(1)

        elif modo == 2:
            jogo.jogar(5)
            
        elif modo == 3:
            break

        else:
            print("Modo de jogo inválido")

if __name__ == "__main__":
    main()
