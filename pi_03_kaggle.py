import pandas as  pd
df = pd.read_csv('2019.csv')
print(df.head())
print(df.columns)
max_index = 0
min_index = 0
for index in df.index:
    print(index)
    if(df['Score'][index] > df['Score'][max_index]):
        max_index = index
    if(df['Score'][index] < df['Score'][min_index]):
        min_index = index

print(df['Country or region'][max_index])
print(df['Country or region'][min_index])

