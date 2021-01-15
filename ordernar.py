import pandas as pd


def sort_arch(self, columns=str):
    df = pd.read_csv('runes.csv')
    df_sorted = df.sort_values([f'{columns}'])
    df_sorted.to_csv('runes.csv')
    
    # 1...2...3...vai filhããooo!!
