import requests  # install requests module using 'pip install requests'

tag = input("gimme tag: ")

url = "https://api.clashofclans.com/v1/players/%23" + tag

# Generate a unique coc api key
key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjA4NDA4NTdkLTk4YTQtNGZjNC1hOTgxLTM0NmQwODY4YzgyOSIsImlhdCI6MTY2NzA0OTY5Mywic3ViIjoiZGV2ZWxvcGVyLzVhMGUzODZhLWM5YTUtNDhhNS0yZDhlLWQyYmE2MmY0ZTQzNyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjM1LjIyMi4yMTkuNDEiXSwidHlwZSI6ImNsaWVudCJ9XX0.y3_2mAwJ4BD0FxDcrWLfDXQccKYLVLB5NgeXlM_TodAZ8S4RlVES4bm8jlQpam6dkUSD_38jKCxRVkO1v0LsvA"

headers = {"Accept": "application/json", "authorization": "Bearer %s" % key}

response = requests.request("GET", url, headers=headers)
data = response.json()
# print(data)
clanName = data['clan']['name']
townHall = data['townHallLevel']
clanRole = data['role']
print(clanName)
print(townHall)
print(clanRole)
