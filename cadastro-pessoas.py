import sqlite3
import emoji
import time


conexao = sqlite3.connect('exercicio.db')
cursor =  conexao.cursor()


def insert_dados():
    cursor = conexao.cursor()
    print('-='*5 ,'INSIRA OS DADOS ', '-='*5)
    nome = input('NOME: ')
    idade = int(input('IDADE: '))
    cidade = input('CIDADE: ')
    valor = [nome, idade, cidade]
    sql = 'Insert into PESSOAS (NOME, IDADE, CIDADE) values (?, ?, ?)'
    print(f'Dados de {nome} inseridos com sucesso. ')

    cursor.execute(sql, valor)
    conexao.commit()

    retornar_menu()

def select_dados():
    cursor = conexao.cursor()
    print('-='*5 ,'REGISTROS CADASTRADOS', '-='*5)
    sql = 'SELECT * FROM PESSOAS'
    print('-='*30)

    consulta = cursor.execute(sql)
    for consultar in consulta:
        print(f'{consultar}')

    retornar_menu()

def select_maior_que_30():
    cursor = conexao.cursor()
    print('-='*5 ,'PESSOAS COM IDADE MAIOR QUE 30 ANOS', '-='*5)
    sql = 'SELECT * FROM PESSOAS WHERE IDADE > 30'
    print('-='*30)

    consulta = cursor.execute(sql)
    for consultar in consulta:
        print(f'{consultar}')

    retornar_menu()

def select_cidade_selecionada():
    cursor = conexao.cursor()
    print('-='*5 ,'PESSOAS QUE MORAM NO RIO DE JANEIRO', '-='*5)
    sql = "SELECT NOME, CIDADE FROM PESSOAS WHERE CIDADE = 'Rio de Janeiro'"

    consulta = cursor.execute(sql)
    for consultar in consulta:
        print(f'{consultar}')

    print('-='*30)
    
    retornar_menu()

def update_idade_pessoa_selecionada():
    cursor = conexao.cursor()
    selecao = cursor.execute('SELECT ID, NOME, IDADE FROM PESSOAS')
    for selecione in selecao:
        print(f'ID: {selecione[0]} | NOME: {selecione[1]} | IDADE: {selecione[2]}')
    
    pessoa_id = int(input('QUAL PESSOA DESEJA ATUALIZAR A IDADE ? '))
    idade = int(input(f'DIGITE A IDADE DE {pessoa_id}: '))
    sql = 'UPDATE PESSOAS SET IDADE = ? WHERE ID = ? '
    valor = [idade, pessoa_id]
    print('Alteração realizada com sucesso ! ')
    print('-='*30)

    cursor.execute(sql, valor)
    conexao.commit()
  
    retornar_menu()
    
def delete_pessoas_menor_que_25():
    cursor = conexao.cursor()
    opcao = input("Você tem certeza ? [S/N]: ")

    if opcao.lower() == 's': 
        sql = 'DELETE FROM PESSOAS WHERE IDADE < 25'
        cursor.execute(sql)
        conexao.commit()
        print('Dados excluídos com sucesso')
        retornar_menu()
    else: 
        print('Operação cancelada')
        retornar_menu()

    conexao.commit()
    conexao.close()

def media_de_idade_pessoas():
    cursor = conexao.cursor()
    print('CONFIRA A MÉDIA DE IDADES DAS PESSOAS CADASTRADAS')
    sql = 'SELECT AVG(IDADE) FROM PESSOAS'

    cursor.execute(sql)

    media_idade = cursor.fetchone()[0]
    print(f'A média de idade é de : {media_idade:.2f} ')

    conexao.commit()

    retornar_menu()

def pessoas_e_cidades(): 
    cursor = conexao.cursor()
    print('LISTA DE PESSOAS JUNTAMENTE COM SUAS CIDADE')
    sql = 'SELECT NOME, CIDADE FROM PESSOAS '

    resultado = cursor.execute(sql)

    for linha in resultado:
        nome_da_pessoa= linha[0]
        nome_da_cidade = linha[1]
        print(f'Nome: {nome_da_pessoa} | cidade: {nome_da_cidade} ' )
        
    conexao.commit()
    retornar_menu()

def media_idade_por_cidade():  
    cursor = conexao.cursor()
    consultar = cursor.execute('SELECT DISTINCT CIDADE FROM PESSOAS')
    for consulta in consultar: 
        print(f'CIDADE: {consulta[0]}')
    
    cidade = input('DIGITE A CIDADE PARA CONSULTA: ')
    sql = "SELECT AVG(IDADE), CIDADE FROM PESSOAS WHERE CIDADE = ?"
    print(f'CONFIRA A MEDIA DE IDADE DO {cidade}')

    resultado = cursor.execute(sql,[cidade])
    for linha in resultado:
        print(f'RESULTADO: {linha}' )

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
    [1] CADASTRAR PESSOA  
    [2] LISTAR PESSOAS 
    [3] PESSOAS COM IDADE MAIOR QUE 30 ANOS
    [4] PESSOAS DO RIO DE JANEIRO
    [5] ATUALIZAR IDADE
    [6] EXCLUIR PESSOAS COM IDADE MENOR QUE 25 ANOS
    [7] MEDIA DE IDADE DAS PESSOAS
    [8] LISTA DE PESSOAS JUNTAMENTE COM SUAS CIDADES
    [9] MEDIA DE IDADE POR CIDADE
    [0] SAIR
    
    QUAL OPÇÃO VOCÊ DESEJA? :  ''' ))

   
    if opcao == 1:
        insert_dados()

    elif opcao == 2: 
        select_dados()

    elif opcao == 3:
        select_maior_que_30()

    elif opcao == 4:
        select_cidade_selecionada()

    elif opcao == 5:
        update_idade_pessoa_selecionada()

    elif opcao == 6:
        delete_pessoas_menor_que_25()

    elif opcao == 7:
        media_de_idade_pessoas()

    elif opcao == 8:
        pessoas_e_cidades()

    elif opcao == 9:
        media_idade_por_cidade()

    elif opcao == 0:
        sair()

    else: 
        print('Opção inválida \n')
        menu()


menu()