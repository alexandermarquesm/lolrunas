linha = 50 * '='
print(linha)
print(f'{"BUSCAR CAMPEÕES":^50}')
print(linha)
print('''[ 1 ] ATUALIZAR BASE DE DADOS
[ 2 ] BUSCAR POR CAMPEÃO
[ 3 ] SAIR''')
while True:
    choice = int(input('ESCOLHA: '))
    print(linha)
    if choice == 1:
        from spider import MainSpider
    elif choice == 2:
        name_champ = str(input('NOME DO CAMPEÃO: '))
        from fetch import Analize
        fetch = Analize('champions')
        champ = fetch.choose_champ(name_champ)[0]
        for c in champ.items():
            print(f'{c[0]:<12}{c[1]}')
    elif choice == 3:
        break
    else:
        print('DIGITE UMA OPÇÃO VÁLIDA')
    print(linha)
