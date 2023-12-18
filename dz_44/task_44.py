import pandas as pd
import random

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
one_hot_data = pd.get_dummies(data['whoAmI'], prefix='whoAmI')
data_one_hot = pd.concat([data, one_hot_data], axis=1)
data_one_hot = data_one_hot.drop('whoAmI', axis=1)
data_one_hot.head()
