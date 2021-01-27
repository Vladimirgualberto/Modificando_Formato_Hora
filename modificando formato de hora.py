import pandas as pd
from datetime import datetime
df = pd.read_excel('C:\\Users\\Vladimir\\PycharmProjects\Relatorio Jeep\\teste1.xlsx')

df['Hora_modificada'] = pd.to_datetime(df['hora'], format= '%H%M') \
                        .apply(lambda x: x.strftime('%H:%M'))


print(df['somente Horas'])

