# Cannot convert non-finite values (NA or inf) to integer

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan', 'Ethan'],
    'salary': [175.1, 180.2, 190.3, 205.4, 210.5],
    'year_joined': [2023.0, 2022.0, None, 2020.0, None],
})

df = df.fillna(value=0)

df['year_joined'] = df['year_joined'].astype(int)

#     name  salary  year_joined
# 0  Alice   175.1         2023
# 1  Bobby   180.2         2022
# 2   Carl   190.3            0
# 3    Dan   205.4         2020
# 4  Ethan   210.5            0
print(df)