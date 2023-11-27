times= {}
x=0
z="-"
while x == 0:
  y=int(input("você deseja\n 1-adicionar novo time\n 2-remover um time\n 3-mostrar os times listados\n 4-adicionar jogador a um time\n 5-remover jogador de um time\n 6-mostrar jogadores de um time especifico\n 7-terminar o programa\n "))
  if y ==1:
    nome_time=input("digite o nome do time:")
    novo_time=[]
    times[nome_time]=novo_time
    print(f"o time {nome_time} foi adicionado]")
    print(z*100)
  elif y == 2:
    print(f"esses são o nome da lista que podem ser removidos{times}")
    nome_time = input("Digite o nome do time a ser removido: ")
    if nome_time in times:
      del times[nome_time]
      print(f"{nome_time}' foi removida.")
      print("times após a remoção:")
      print(times)
      print(z*100)
    else:
      print("A chave fornecida não existe no dicionário.")
      print(z*100)
  elif y == 3:
    print(f"esses são os times que estão listados {times}\n")
    print(z*100)
  elif y == 4:
    print(f"esses são os times disponiveis para adicionar jogadores:{times}")
    nome_time=input("digite o nome do para qual você deseja adicionar o jogador:")
    if nome_time in times:
      nome_jogador = input("Digite o nome do jogador: ")
      times[nome_time].append(nome_jogador)
      print(f"O jogador {nome_jogador} foi adicionado ao time {nome_time}.")
      print(z*100)
    else:
      print("O time fornecido não existe.")
      print(z*100)
  elif y == 5:
    print(f"esses são os times disponiveis para adicionar jogadores e seus respectivos jogadores:{times}")
    nome_time=input("digite o nome do time para qual você deseja remover o jogador:")
    if nome_time in times:
      print(f" esses são os jogadores que estão disponivel no time que você escolheu{times[nome_time]}")
      nome_jogador = input("Digite o nome do jogador: ")
      if nome_jogador in times[nome_time]:
        times[nome_time].remove(nome_jogador)
        print("jogador removido com sucesso")
        print(z*100)
      else:
        print("jogador não encontrado")
        print(z*100)
    else:
      print("O time fornecido não existe.")
      print(z*100)
  elif y == 6:
    print(f"esses são os nomes dos times:")
    for chaves in times.keys():
      print(chaves)
    nome_time=input("digite o nome do time qual você deseja ver os jogadores:")
    print(f" esses são os jogadores que estão disponivel no time que você escolheu{times[nome_time]}")
    print(z*100)

  elif y== 7:
    print("fim do programa")
    print(z*100)
    x+=1
  else:
    print(" opção incorreta!")
    print(z*100)
