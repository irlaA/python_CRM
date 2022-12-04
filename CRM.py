#Importaciones.
from re import X
from turtle import clear
import pandas as pd
import numpy as np
import os

# Função para limpar o console.
clear_output = lambda: os.system('cls')

#Menu principal
def menu():
    print("========================")
    print()
    print("Selecione uma opção:")
    print()
    print("(1) Clientes.")
    print("(2) Produtos.")
    print("(3) Notas.")
    print("(4) Finalizar.")
    print()
    print("========================")

    #Valor de entrada.
    x = int(input("Escolher um número entre as opções"))

    #Opção 1
    if x == 1: 
      clear_output()
      print("========================")
      print()
      print("Inicio > Clientes")
      print()
      print("(1) Consultar lista de clientes.")
      print("(2) Adicionar um cliente.")
      print("(3) Voltar ao menu principal.")
      print()
      print("========================")
      # Valor de entreda Opção 1 > Menu 2
      MenuOp1 = int(input("Escolha uma opção: "))
      #Clientes > Ler base de dados
      if MenuOp1 == 1:
        clear_output()
        tabla_clientes = pd.read_csv('clientes.csv')
        print(tabla_clientes)
        print()
        menu()    
      #Clientes > Add novo cliente
      elif MenuOp1 == 2: 
        clear_output()
        print("========================")
        print()
        print("(+) Por favor escreva os seguintes dados.")
        name = input("Nome completo do cliente: ")
        date = input("Data de cadastro do cliente: ")
        id = input("Id atribuido ao cliente: ")
        mail = input("Email do cliente: ")
        clientes = {'Nome':[name],
                    'Data_de_registro':[date],
                    'Id':[id],
                    'Email':[mail],
        }
        clear_output()
        print("O cliente foi registrado com os seguintes dados:  ", clientes)
        print()
        print("Para confirmar escolha 1, para cancelar escolha 2")
        #Confirmar Registro cliente.
        MenuConfirmar = int(input("Confirmar? "))
        #Confirmar, anexar cliente a base de dados
        if MenuConfirmar == 1:
          clear_output()
          print(clientes)
          print()
          myDS1 = pd.DataFrame(clientes)
          print(myDS1)
          myDS1.to_csv('clientes.csv')
          print()
          print("Os dados foram armazenados com sucesso!")
          print()
          menu()
        #Rejeitar, excluir dados de registro.
        elif MenuConfirmar == 2: 
          clear_output()
          clientes = {}
          menu()
        #Opção invalida.
        else:
          clear_output()
          print("Opção inválida, retornando ao menu principal")
          menu()

      #Clientes > Voltar ao menu principal
      elif MenuOp1 == 3:
        clear_output()
        menu ()          

    #Procedimiento Opção 2
    elif x == 2: 
      clear_output()
      print("========================")
      print()
      print("Inicio > Procedimento")
      print()
      print("(1) Consultar procedimentos.")
      print("(2) Adicionar um procedimento novo.")
      print("(3) Voltar ao menu principal.")
      print()
      print("========================")
      # Voltar ao menu principal Opção 2 > Menu 2
      MenuOp2 = int(input("Escolha uma opção: "))
      #Productos > Leer Base de datos
      if MenuOp2 == 1:
        clear_output()
        tabla_productos = pd.read_csv('productos.csv')
        print(tabla_productos)
        print("")
        menu()
      #Produtos > add nota a base dedos
      elif MenuOp2 == 2: 
        clear_output()
        print("(+) Por favor complete os siguintes dados.")
        name = input("Informe o tipo de procediemente: ")
        id = input("Informe o id atribuido ao procedimento: ")
        price = int(input("Informe o valor unitário referente ao procedimento: "))
        desc = input("Informa uma breve descrição do procedimento: ")
        productos = {'Nome_procedimento':[name],
                     'Id':[id],
                     'Valor':[price],
                     'Descrição':[desc]
      }
        clear_output()

        print("O procedimento será registrado com os seguintes dados:  ", productos)
        print()
        print("Para confirmar escolha 1, para cancelar escolha 2")
        #Confirmar Registro nota.
        MenuConfirmar = int(input("Confirmar? "))
        #Confirmar, anexar procedimento a base de dados
        if MenuConfirmar == 1:
          clear_output()
          print(productos)
          print()
          myDS2 = pd.DataFrame(productos)
          print(myDS2)
          myDS2.to_csv('productos.csv')
          print()
          print("Os dados foram armazenados com sucesso!")
          print()
          menu()
        #Rejeitar, excluir dados de registro.
        elif MenuConfirmar == 2: 
          clear_output()
          productos = {}
          menu()
        #Opção inválida.
        else:
          clear_output()
          print("Opção inválida, retornando ao menu principal")
          menu()
       
      #Produtos > voltar ao menu principal
      elif MenuOp2 == 3: 
        clear_output()
        menu() 
      #Produtos > opção invalida
      else:
        clear_output()
        print("Opção inválida, retornando ao menu principal")
        menu()

    #Procedimiento Opción 3
    elif x == 3: 
      clear_output()
      print("========================")
      print()
      print("Inicio > Notas")
      print()
      print("(1) Consultar notas.")
      print("(2) Adcionar uma nota.")
      print("(3) Voltar ao menu principal.")
      print()
      print("========================")
      # Valor de entrada Opção 1 > Menu 3
      MenuOp3 = int(input("Escolha uma opção: "))
      # Notas > Exibir base de dados
      if MenuOp3 == 1: 
        clear_output()
        print("Lista de notas registradas")
        tabla_notas = pd.read_csv('notas.csv')
        print()
        print(tabla_notas)
        print()
        menu()
      #Notas > criar nova nota
      elif MenuOp3 == 2:
          print("(+) Por favor complete os siguintes dados.")
          name = input("Nome do cliente: ")
          clv = input("Chave (id) do item: ")
          art = int(input("Numero de itens comprados: "))
          if art < 0:
            print("Erro, números negativos não são aceitos.")
            print()
            print("Voltar ao menu principal.")
            menu()
          prc = int(input("Preçõ por unidade do produto comprado: "))
          if prc < 0:
            print("Erro, números negativos não são aceitos.")
            print()
            print("Voltar ao menu principal.")
            menu()
          totalp = prc * art
          notas = {'Nota':[name],
                     'Numero_de_itens':[art],
                     'id_item':[clv],
                     'preco_uni':[prc],
                     'preco_total':[totalp]
            }
          clear_output()
          print("O total a pagar é: ", totalp, "R$.")
          print("A nota será resgitrada com os seguintes dados:  ", notas)
          print()
          print("Para confirmar escolha 1, para cancelar escolha 2")
        #Confirmar Registro nota.
          MenuConfirmar = int(input("Confirmar?: "))
        #Confirmar, adjuntar cliente a base de datos.
          if MenuConfirmar == 1:
            clear_output()
            print()
            myDS3 = pd.DataFrame(notas)
            myDS3.to_csv('notas.csv')
            print()
            print("Os dados foram armazenados com sucesso!")
            print()
            menu()
          #Rechazar, borrar datos de registro.
          elif MenuConfirmar == 2: 
            clear_output()
            Notas = {}
            menu()
          #Opción no válida.
          else:
            clear_output()
            print("Opção inválida, retornando ao menu principal")
            menu()

      #Notas > Regresar al Menú principal
      elif MenuOp3 == 3:  
        clear_output()
        menu() 

      #Notas > Opción invalida
      else:
        clear_output()
        print("Opção inválida, retornando ao menu principal")
        print()
        menu()

    #Procedimiento Opción 4
    elif x == 4: 
      clear_output()
      print("========================")
      print()
      print("Obrigado por utilizar este sistema.")
      print("Tenha um bom dia:)")
      print()
      print("========================")

    #Procedimiento Opción No Valida.
    else:
      print()
      print("ERROR:")
      print("Opção inválida, escolher ente 1 e 4")
      print()
      menu ()

#Invocar Función
menu()