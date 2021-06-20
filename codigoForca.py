#código desenvolvido por Helen Deuner Ferreira e Lênisson Nasiloski Bebber

LC_CTYPE = "UTF-8"

import os
import time
#import sys

def telaLimpa():
    os.system("cls")

def split_str(s):
    return [ch for ch in s]

def pulaLinha():
    print("\n")

print("=== Bem-vindo ao Jogo da Forca! ===")
pulaLinha()

print("Regras: o desafiante escolherá a palavra-chave e fornecerá 3 dicas para o competidor. O competidor precisa adivinhar as letras que compõem a palavra-chave. Se o competidor errar 5 vezes, ele perde e o desafiante ganha; caso contrário, o desafiante perderá e o competidor ganhará.")
pulaLinha()

nomeCompetidor = input("Informe o nome do competidor: ")
nomeDesafiante = input("Informe o nome do desafiante: ")

telaLimpa()

print("=== Seção exclusiva para o desafiante ===")
pulaLinha()

palavraChave = input("Digite a palavra chave: ")
dica1 = input("Dica 1: ")
dica2 = input("Dica 2: ")
dica3 = input("Dica 3: ")

todasAsDicas = [dica1, dica2, dica3]

palavraMisteriosa = "*" * len(palavraChave)
print("Palavra: ", palavraMisteriosa)

telaLimpa()

listaDeLetras = split_str(palavraChave)
listaDeLetrasMisteriosas = split_str(palavraMisteriosa) 

def vencedorDosJogos():
    jogadorVencedor = True
    i = 0

    global vencedor
    global perdedor

    pararJogo = False

    if erros == 5:
        vencedor = nomeDesafiante
        perdedor = nomeCompetidor
        print("O Jogo acabou. O vencedor é ", nomeDesafiante)

    else:       
      for i in listaDeLetrasMisteriosas:
        if i == '*':
          jogadorVencedor = False  

      if jogadorVencedor:
        vencedor = nomeCompetidor
        perdedor = nomeDesafiante
        print("O Jogo acabou. O vencedor é ", nomeCompetidor)

    if vencedor > " ":
        pararJogo = True
        
    return pararJogo        

def chutaLetra(erros):
    erroSomado = 0
    letraChutada = input("Chute uma letra: ")
    acerto = False
    for i in range(0, len(listaDeLetras), 1):
        if letraChutada == listaDeLetras[i]:
            listaDeLetrasMisteriosas[i] = letraChutada
            exibicaoLista = "".join(listaDeLetrasMisteriosas)
            acerto = True
            
    if acerto == True:
        print("Você acertou!")
        print(exibicaoLista) 
    else: 
        erroSomado = erros + 1 
        if erroSomado > 0:   
            print("Você errou: ", erroSomado, "vezes!")

    return erroSomado
    
def criarAquivosJogos():
    arquivoJogos = open("AquivoDasJogadas.txt", "a")
    arquivoJogos.write(f"Vencedor: {vencedor} - Perdedor: {perdedor} - Palavra: {palavraChave}\n")
    arquivoJogos.close()
    arquivoJogos = open("AquivoDasJogadas.txt", "r")
    historico = arquivoJogos.read()
    arquivoJogos.close()

    return historico

erros = 0

while True:     
    vencedor = " "
    pararJogo = False

    def jogadaCompetidor():
        global erros
        print("Palavra: ", listaDeLetrasMisteriosas)
        jogada = input("Competidor, você deseja uma dica ou tentar a primeira jogada? Escreva 'dica' ou 'tentar': ")
        
        if jogada == "dica":
            contadorDicas = int(len(todasAsDicas))

            while True:
                if contadorDicas == 3:
                    print("A dica 1 é", todasAsDicas[0])
                    time.sleep(0.5)
                    contadorDicas -= 1
                    del(todasAsDicas[0])
                    break

                elif contadorDicas == 2:
                    print("A dica 2 é", todasAsDicas[0])
                    time.sleep(0.5)
                    contadorDicas -= 1
                    del(todasAsDicas[0])
                    break

                elif contadorDicas == 1:
                    print("A dica 3, e a última, é", todasAsDicas[0])
                    time.sleep(0.5)
                    contadorDicas -= 1
                    del(todasAsDicas[0])
                    break
                    
                else: 
                    print("Suas dicas acabaram, chute uma letra!")
                    chutaLetra(erros)
        else:
            erros = chutaLetra(erros)
    
    jogadaCompetidor()
    pararJogo = vencedorDosJogos()

    if pararJogo:
        try:
            historico = criarAquivosJogos()
        except:
            print("Não foi possível armazenar o histórico das jogadas.")

        print(historico)
        break

reiniciar = input("Deseja jogar novamente? S ou N:")

if reiniciar == "S":
    os.system("python jogoForca.py")
else:
    telaLimpa()
    exit(0)