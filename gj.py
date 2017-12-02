import time
count=0
f=0
for i in range (100):
	#time.sleep(1)
	import requests
	import json

	# This is the url to which the query is made
	url = "https://data.bureaucrat75.hasura-app.io/v1/query"

	# This is the json payload for the query
	requestPayload = {
	    "type": "update",
	    "args": {
	        "table": "Issue_tab",
	        "where": {},
	        "$set": {},
	        "$inc": {
	            "days_to_go": "-1"
	        }
	    }
	}

	# Setting headers
	headers = {
	    "Content-Type": "application/json"
	}

	# Make the query and store response in resp
	resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

	# resp.content contains the json response.
	#print(resp.content)

	requestPayload = {
    "type": "select",
    "args": {
        "table": "Issue_tab",
        "columns": [
            "*"
        ]
    }
	}

	# Setting headers
	headers = {
	    "Content-Type": "application/json"
	}

	# Make the query and store response in resp
	resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

	# resp.content contains the json response.
	#print(resp.content)
	data=resp.json()
	print(data)
	print("asdfasdfasdf" ,len(data))

	for i in range(len(data)):
		dtg=data[i]['days_to_go']
		print(i,dtg)
		if dtg==0:
		
			# update query###########
			current_level=data[i]['Level']
			current_level=current_level+1
			url = "https://data.bureaucrat75.hasura-app.io/v1/query"

			# This is the json payload for the query
			requestPayload = {
			    "type": "select",
			    "args": {
			        "table": "operational_personel",
			        "columns": [
			            "Personel_name"
			        ],
			        "where": {
			            "level":str(current_level)
			        }
			    }
			}

			
			# Setting headers
			headers = {
			    "Content-Type": "application/json"
			}

			# Make the query and store response in resp
			resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

			# resp.content contains the json response.
			print(resp.content)
			data=resp.json()
			op=data[0]["Personel_name"]

			print("updated person", op)



			url = "https://data.bureaucrat75.hasura-app.io/v1/query"

			# This is the json payload for the query
			requestPayload = {
			    "type": "update",
			    "args": {
			        "table": "Issue_tab",
			        "where": {},
			        "$set": {
			        "current_personel":str(op),
			        "days_to_go":"3"
			        },
			        "$inc": {
			            "Level": "1"
			        }
			    }
			}

			# Setting headers
			headers = {
			    "Content-Type": "application/json"
			}

			# Make the query and store response in resp
			resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

			# resp.content contains the json response.
			print(resp.content)

					

			global count 
			count = count+ 1
			("count",count)
		if count==len(data):
			f=1
			break
	if f==1:
		break

