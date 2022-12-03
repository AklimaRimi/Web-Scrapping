import requests
import bs4
import pandas as pd

url = 'https://en.wikipedia.org/wiki/FIFA_World_Cup'

html = bs4.BeautifulSoup(requests.get(url,{}).text,'lxml')

# print(html)

tables = html.find_all('table')

print('>>>>>>>>>>>>>>>>')
# print(tables[3])

t_rows = tables[3].find_all('tr')

cols = [name.text.replace('\n','') for name in t_rows[0].find_all('th')]

cols.pop()

for i in t_rows[1].find_all('th'):
    cols.append("highest attendence of " + i.text.replace('\n',''))
years = [i.text for i in t_rows[2].find_all('td')]
print(years)

datas = []
for i in range(2,len(t_rows)-1):
    datas.append([data.text.replace('\n','') for data in t_rows[i].find_all('td')])
    
    
    


print(datas)
dataframe = pd.DataFrame(datas,columns=cols)
print(dataframe.head(4))

dataframe.to_csv('FIFA World Cup.csv',index = False)