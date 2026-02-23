from random import randint
from time import sleep

#Função do modo de jogo que está pronto
def jogar(qntdDeRodadas):

    #Contar as rodadas
    contadorDeRodadas = 0
    #Contar os pontos do Jogador
    pontosJ = 0
    #Contar os pontos do Computador
    pontosC = 0
    #Para armazenar em indices para manipular qual será a escolha baseada no número
    jokempo = ["Pedra", "Papel", "Tesoura"]

    while True:
        
        #verificação do contador para encerrar o loop do jogos
        if contadorDeRodadas == qntdDeRodadas:
            break
        
        #Gerar um número de 0 a 2 para lançar qual foi a escolha
        computador = randint(0,2)
        
        #Para pedir que o usuário coloque a informação que está sendo pedida 
        try:
            jogador = int(input("\nEscolha uma opção entre essas: \n[1]Pedra \n[2]Papel \n[3]Tesoura \n-> "))
        except ValueError:
            print("Escolha entre uma dessas opções numeradas\n")
            continue
        
        #Verificação se o jogador inseriu um número dentro do intervalo
        if 1 <= jogador <= 3:
            
            #Esse "Jogador -= 1" é para entra no intervalo de indice da lista "jokempo"
            jogador -= 1

            #Verificar a condição de empate
            if jogador == computador:
                sleep(0.5)
                print("")
                print("-="*11)
                print(f"{jokempo[jogador]}\n{jokempo[computador]}")
                print("-="*11)
                sleep(0.5)
                print(f"Empate!!\n")

                #Contador de rodadas aumentando para poder parar o loop
                contadorDeRodadas += 1

                
                
            #Verifica a condição de vitória do jogador
            # [0]Pedra, [1]Papel, [2]Tesoura
            elif(jogador == 0 and computador == 2) or \
                (jogador == 1 and computador == 0) or \
                (jogador == 2 and computador == 1):
                sleep(0.5)
                print("")
                print("-="*11)
                print(f"{jokempo[jogador]}\n{jokempo[computador]}")
                print("-="*11)
                sleep(0.5)
                print("Você venceu!!!!\n")

                #Contador de rodadas aumentando para poder parar o loop
                contadorDeRodadas += 1
                
                #Contar os pontos do Jogador
                pontosJ += 1
            
            #Verifica a condição de derrota do jogador
            else:
                sleep(0.5)
                print("")
                print("-="*11)
                print(f"{jokempo[jogador]}\n{jokempo[computador]}")
                print("-="*11)
                sleep(0.5)
                print("Que pena, você perdeu! :(\n")

                #Contador de rodadas aumentando para poder parar o loop
                contadorDeRodadas += 1
                
                #Contar os pontos do Computador
                pontosC += 1

            #Condição para verificar empate para uma rodada de desempate
            if contadorDeRodadas >= 3 and pontosC == pontosJ:
                print(f"Jogador/Computador \n{pontosJ}     /  {pontosC}")
                print("Empates não são permitidos aqui!!")
                contadorDeRodadas -= 1
                
            elif contadorDeRodadas >= 3 and pontosC > pontosJ:
                if pontosC > 3:
                    print(f"Jogador/Computador \n{pontosJ}     /  {pontosC}")
                    print("Computador ganhou!!")
                
            elif contadorDeRodadas >= 3 and pontosC < pontosJ:
                if pontosJ > 3:
                    print(f"Jogador/Computador \n{pontosJ}     /  {pontosC}")
                    print("Você ganhou!!")
                    
                else:
                    continue

        #Mensagem para o usuário inserir um número dentro do intervalo
        else:
            print("\nInsira um número dentro do intervalo entre 1 e 3")

    #Placar do Jogador e do Computador
    print(f"Jogador/Computador \n{pontosJ}     /  {pontosC}")