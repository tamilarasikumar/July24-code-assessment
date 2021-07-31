import json
import requests
try:
    data=requests.get("https://jsonplaceholder.typicode.com/todos")
    ED=data.json()
    #print(ED)
    Empty_List=[]
    List_Of_TrueData=[i for i in ED if i["completed"]==True]
    #lis1=[j["completed"] for j in lis if j['completed']==True ]
    Empty_List.append(List_Of_TrueData)
    print(Empty_List)

except:
    print("oops, please check the link again")

else:
    print("We got details who has completed = true")

finally:
    print("Good job, question 1 is completed ")
