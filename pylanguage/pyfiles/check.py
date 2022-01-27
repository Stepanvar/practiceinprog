import pandas as pd
import re

df = pd.DataFrame([[10, 3, 6], [9, 6, 9]])
df.loc[df[1] % 2 == 0, [1]] = 10
print(df)
stri = "hellomy7173"
print(re.search(r'5', stri))