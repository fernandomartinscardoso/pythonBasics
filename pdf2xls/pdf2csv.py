from tabula.io import read_pdf, convert_into
df = read_pdf('data.pdf', pages="all", lattice=True)[1]
print(df)
convert_into('data.pdf', 'data.csv', pages="all", output_format='csv', java_options=None, guess=False)
#df.columns = df.columns.str.replace('\r', ' ')
#data = df.dropna()
#data.to_excel('data.xlsx')
