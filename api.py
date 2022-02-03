import requests

class helper : 
    def main(list, name):
        for i in list:
            for j in i:
             if j == name:
                print(f'{name} : {i[j]}')

    def desc(list, name): 
        for i in list:
            for j in i:
             if j == name:
                print(f'{name} : {i[j]}')
    def sys(list, name):
        for i in list:
            if i == name:
                print(f'{name} : {list[name]}')
           

API_KEY = '9a9acc484e9827ea11576372f2e24211'
City = input('Enter City name : ')
URL = f'http://api.openweathermap.org/data/2.5/weather?q={City}&appid={API_KEY}'
r = requests.get(URL)

r_json = r.json()
arr = r_json['weather']
sys = r_json['sys']



if r.ok :
 
    helper.main(arr, 'main')
    helper.desc(arr,'description')
    helper.sys(sys, 'country')
            
            
   
else :
    print('An error has occured')










