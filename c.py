#entering the all the commit details in the repository(multiple pages)

import re
import json
import requests

name=[]
msg=[]
author=[]
date=[]

import csv
with open('commits4.csv', 'w', newline= '') as f:
    f_names=['Commit Name', 'Commit Mesage', 'Commit Author', 'Commit Date&Time']
    thewriter = csv.DictWriter(f, fieldnames=f_names)
    thewriter.writeheader()

    for j in range(1,4):
        #print(j)
        commit=requests.get('https://api.bitbucket.org/2.0/repositories/bmsce2019ccplabph/ph48/commits/?page=%d'%j)
        #commit=requests.get('https://api.bitbucket.org/2.0/repositories/bmsce2019ccplabph/ph48/commits')
        d=commit.json()
        #print(d['values'])

        for i in range(len(d['values'])):
            x1=requests.get(d['values'][i]['links']['self']['href'])
            d1=x1.json()
            x2= requests.get(d['values'][i]['links']['diff']['href'])
            d2=x2.text
            m=re.match(r"^diff --git a/(.*) b",d2)
            
            cname=m.groups(1)[0]
            cmsg=d1['message']
            cauthor=d1['author']['raw']
            cdate=d1['date']
            
            name.append(cname)
            msg.append(cmsg)
            author.append(cauthor)
            date.append(cdate)
            
            #print(d1['message'])
            
            thewriter.writerow({'Commit Name':cname, 'Commit Mesage':cmsg, 'Commit Author':cauthor, 'Commit Date&Time':cdate})

    f.close()

print(len(name),len(msg),len(author),len(date))
