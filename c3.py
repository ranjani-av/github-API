#entering the all the commit msgs in the repository(multiple pages)

#import re
import json
import requests

msg=[]

import csv
with open('commits3.csv', 'w', newline= '') as f:
    f_names=['Commit Mesage']
    thewriter = csv.DictWriter(f, fieldnames=f_names)
    thewriter.writeheader()

    for j in range(1,4):
        print(j)
        commit=requests.get('https://api.bitbucket.org/2.0/repositories/bmsce2019ccplabph/ph48/commits/?page=%d'%j)
        #commit=requests.get('https://api.bitbucket.org/2.0/repositories/bmsce2019ccplabph/ph48/commits')
        d=commit.json()
        print(d['values'])

        for i in range(len(d['values'])):
            x1=requests.get(d['values'][i]['links']['self']['href'])
            d1=x1.json()
            cmsg=d1['message']
            msg.append(cmsg)
            #print(d1['message'])
            thewriter.writerow({'Commit Mesage':cmsg})

    f.close()

print(len(msg))

    
