import pandas as pd
from datetime import datetime


df = pd.read_csv('C:\\Users\\Vladimir\\PycharmProjects\\relatorio_toyolex\\dados_A001.csv',skiprows=10, sep=';',dtype=str)



df['Hora_modificada'] = pd.to_datetime(df['Hora Medicao'], format= '%H%M') \
                      .apply(lambda x: x.strftime('%H:%M'))


print(df['Hora_modificada'])