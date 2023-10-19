import sqlite3
import emoji
import time


conexao = sqlite3.connect('exercicio.db')
cursor =  conexao.cursor()

def insert_hobbies():
    cursor = conexao.cursor()
    selecao = cursor.execute('SELECT ID, NOME FROM PESSOAS')
    for selecione in selecao: 
        print(f'ID: {selecione[0]} | NOME: {selecione[1]} ')
   
    pessoa_id = int(input('ESCOLHA O ID PARA ADICIONAR UM HOBBIE: '))
    hobbie = input(f'DESCREVA O HOBBIE DA PESSOA {pessoa_id}: ')
    sql = 'INSERT INTO HOBBIES (PESSOA_ID , HOBBY) VALUES (?, ?)'
    valor = [pessoa_id , hobbie]
    print('Dados inseridos com sucesso ! ')

    cursor.execute(sql, valor)
    conexao.commit()

    retornar_menu()

def pessoas_e_hobbies():
    cursor = conexao.cursor()
    print('LISTA DE PESSOAS E SEUS HOBBIES')
    sql = '''SELECT P.NOME, H.HOBBY 
    FROM PESSOAS AS P 
    INNER JOIN HOBBIES AS H ON P.ID = H.PESSOA_ID'''

    cursor.execute(sql)

    resultado = cursor.fetchall()

    for linha in resultado:
        nome_da_pessoa, hobby = linha
        print(f'Nome: {nome_da_pessoa} | Hobby: {hobby}')

    conexao.commit()
   
    retornar_menu()

def hobby_especifico():
    cursor = conexao.cursor()
    hobby_especifico = input('HOBBY: ')
    sql = '''SELECT P.NOME AS NomeDaPessoa
    FROM PESSOAS AS P 
    INNER JOIN Hobbies AS H ON P.ID = H.PESSOA_ID
    WHERE H.Hobby = ? ;'''

    cursor.execute(sql, (hobby_especifico,))
    resultado = cursor.fetchall()

    print(f'Pessoas que possuem o hobbie de {hobby_especifico} ')
    for linha in resultado:
        nome_da_pessoa= linha[0]
        print(f'Nome: {nome_da_pessoa} ' )

    conexao.commit()
   
    retornar_menu()

def hobbies_em_comum():
    cursor = conexao.cursor()
    resultado = cursor.execute('SELECT NOME FROM PESSOAS')
    for result in resultado:
        print(f' NOME {result[0]}')
    
    nome = input('DIGITE O NOME DESEJADO: ')
    sql = f''' SELECT DISTINCT P.NOME FROM PESSOAS AS P INNER JOIN HOBBIES H
         ON P.ID = H.PESSOA_ID WHERE H.HOBBY IN 
         (SELECT HOBBY FROM HOBBIES H 
         INNER JOIN PESSOAS P ON P.ID= H.PESSOA_ID WHERE P.NOME = '{nome}')
        '''

    pessoas_hobbies_em_comum = cursor.execute(sql)
    print(F'PESSOAS COM HOBBIES EM COMUM COM {nome} ')

    for phc in pessoas_hobbies_em_comum:
        print(f'NOME: {phc[0]} ')
    
    conexao.commit()
    
    retornar_menu()

def retornar_menu():
    opcao = int(input('''Deseja retornar ao menu ? 
    [1] Sim 
    [2] Não 
    Escolha um número: '''))

 
    if opcao == 1:
        menu()
    elif opcao == 2:
        sair()
    else: 
        print('Opção inválida \n')
        retornar_menu()

def sair():
    print('Saindo do programa em ')
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print(emoji.emojize('Até a próxima ! :waving_hand:  ', language='en'))


def menu():
    opcao= int(input('''
    "ESCOLHA UMA DAS OPÇÕES:
    [1] INSERIR HOBBY
    [2] LISTAR PESSOAS E HOBBIES
    [3] HOBBY ESPECÍFICO
    [4] PESSOAS COM HOBBY EM COMUM
    [0] SAIR
    
    QUAL OPÇÃO VOCÊ DESEJA? :  ''' ))

   
    if opcao == 1:
        insert_hobbies()

    elif opcao == 2: 
        pessoas_e_hobbies()

    elif opcao == 3:
        hobby_especifico()

    elif opcao == 4:
        hobbies_em_comum()

    elif opcao == 0:
        sair()

    else: 
        print('Opção inválida \n')
        menu()


menu()
