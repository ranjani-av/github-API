# entering name, msg, author, time of the latest commit into csv file
import json
import requests

commit=requests.get('https://api.bitbucket.org/2.0/repositories/bmsce2019ccplabph/ph48/commits')	
d=commit.json()
#d['values'][0]['links']
x1=requests.get(d['values'][0]['links']['self']['href'])
d1=x1.json()

x2= requests.get(d['values'][0]['links']['diff']['href'])
d2=x2.text
#print(d2)
import re
m=re.match(r"^diff --git a/(.*) b",d2)
#m.groups(1)[0]

import csv
commit_name=m.groups(1)[0]
msg=d1['message']
commit_author=d1['author']['raw']
commit_date=d1['date']
with open('commits1.csv', 'w', newline= '') as f:
	f_names=['Commit name', 'commit mesage', 'commit author', 'Commit date&time']
	thewriter = csv.DictWriter(f, fieldnames=f_names)
	thewriter.writeheader()
	thewriter.writerow({'Commit name':commit_name, 'commit mesage':msg, 'commit author':commit_author, 'Commit date&time':commit_date})
	f.close()
