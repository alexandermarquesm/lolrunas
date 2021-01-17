from typing import List, Dict


class GUI:
    def __init__(self, options: List[Dict[int, str]]):
        self.options = options
        self.linha = 50 * '\033[30;40m=\033[m'


    @staticmethod
    def update_db():
        from spider import MainSpider
        from scrapy.crawler import CrawlerProcess
        miranha = CrawlerProcess()
        miranha.crawl(MainSpider)
        miranha.start()
        print('DATA BASE ATUALIZADO')

    @staticmethod
    def fetch(name_champ: str):
        from fetch import Analize
        fetch = Analize('champions')
        champ = fetch.choose_champ(name_champ)[0]
        for c in champ.items():
            print(f'{c[0]:<15}{c[1]}')

    def exist_or(self, op: int):
        if self.search_op(op):
            return op
        else:
            print('\033[1;31mDIGITE UMA OPÇÃO VÁLIDA\033[m')

    def search_op(self, value):
        for v in self.options:
            if v.get(value):
                return value

    def create_gui(self):
        print(self.linha)
        for op in self.options:
            for k, v in op.items():
                str_option = f'[ {k} ]  {v}'
                print(str_option)
        print(self.linha)

    def main(self):
        while True:
            self.create_gui()
            op = int(input('DIGITE A OPÇÃO: '))
            if self.exist_or(op):
                if op == 1:
                    while True:
                        print(self.linha)
                        op = input('\033[1;32mVOCÊ TEM CERTEZA QUE QUER ATUALIZAR O DB? [Y/N]: \033[m')
                        if op.lower() == 'y':
                            self.update_db()
                            break
                        elif op.lower() == 'n':
                            break
                        else:
                            print(self.linha)
                            print('\033[1;31mDIGITE UM OPÇÃO CORRETA\033[m')
                elif op == 2:
                    while True:
                        try:
                            print(self.linha)
                            op = input('NOME DO CAMPEÃO: ')
                            self.fetch(op)
                        except IndexError:
                            if op.lower() in ['sair', 'exit', '3']:
                                break
                            print('\033[1;31mDIGITE O NOME DO CAMPEÃO CORRETAMENTE\033[m')
                if op == 3:
                    print('\033[1;34mCY@\033[m')
                    print(self.linha)
                    break


too = GUI([
    {1: 'ATUALIZAR BASE DE DADOS'},
    {2: 'BUSCAR POR CAMPEÃO'},
    {3: 'SAIR'}
])

too.main()
