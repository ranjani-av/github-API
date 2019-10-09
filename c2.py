#entering the commit msgs of the first page
import re
import json
import requests
commit=requests.get('https://api.bitbucket.org/2.0/repositories/bmsce2019ccplabph/ph48/commits')
d=commit.json()

msg=[]

import csv
with open('commits2.csv', 'w', newline= '') as f:
    f_names=['Commit Mesage']
    thewriter = csv.DictWriter(f, fieldnames=f_names)
    thewriter.writeheader()

    for i in range(len(d['values'])):
        x1=requests.get(d['values'][i]['links']['self']['href'])
        d1=x1.json()
        cmsg=d1['message']
        msg.append(cmsg)
        #print(d1['message'])
        thewriter.writerow({'Commit Mesage':cmsg})

    f.close()

print(len(msg))

    
