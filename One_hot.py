import pandas as pd
import random
# Создаем DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

# Преобразуем в one-hot encoding
one_hot_encoded = pd.get_dummies(data['whoAmI'])

# Объединяем с исходным DataFrame
data_encoded = pd.concat([data, one_hot_encoded], axis=1)

# Удаляем исходный столбец 'whoAmI'
data_encoded.drop('whoAmI', axis=1, inplace=True)

data_encoded.head()
