import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
data.loc[data['whoAmI'] == 'human'] = 1
data.loc[data['whoAmI'] == 'robot'] = 0

print(data)