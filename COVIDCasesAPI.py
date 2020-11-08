import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"
##needs api key
apiKey = ""

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': apiKey
    }

response = requests.request("GET", url, headers=headers)


content = response.content
info = json.loads(content)
print(type(info))
print(info)

virus =  open('CV2020.csv', 'w')

responsej = info['response']
virus.write('Country' + ',' + 'New Cases' + ','+ 'Active Cases'+ ','+ 'Critical Cases'+ ','+'Recovery'+ ','+'New Deaths'+ ','+'Total Deaths' +'\n')
for i in range(0, len(responsej)):
    responseInfo = responsej[i]
    country = responseInfo['country']
    
    cases = responseInfo['cases']
    deaths = responseInfo['deaths']

    new = cases['new']
    active = cases['active']
    critical = cases['critical']
    recovered = cases['total']

    newDeaths = deaths['new']
    totalDeaths = deaths['total']

    if(newDeaths == None):
        newDeaths = '0'

    if(new== None):
        new = '0'

    if(country=='All'):
        continue


    
    virus.write(country + ',' + new + ',' + str(active)+ ',' + str(critical)+ ',' + str(recovered)+ ',' + str(newDeaths)+ ',' + str(totalDeaths) +'\n')
    print(country + ',' + new + ',' + str(active)+ ',' + str(critical)+ ',' + str(recovered)+ ',' + str(newDeaths)+ ',' + str(totalDeaths))

virus.close()

