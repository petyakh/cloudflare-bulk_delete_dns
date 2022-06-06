import requests, json

# API Token could be set at https://dash.cloudflare.com/profile/api-tokens
token = "<API TOKEN OF YOUR CLOUDFLARE ACCOUNT>"

# You can obtain it on the "Overview" tab of your domain
# (the very first tab, that is a dashboard for the domain)
zone = "<YOUR DOMAIN ZONE>"

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json',
}

params = {
    'page': '1',
    'per_page': '300',
}

response = requests.get('https://api.cloudflare.com/client/v4/zones/' + zone + '/dns_records', params=params, headers=headers)
data = json.loads(response.text)
#print(data['result'])


for record in data['result']:
    thisrecordid = record['id']
    print(thisrecordid)
    deldns = requests.delete('https://api.cloudflare.com/client/v4/zones/' + zone + '/dns_records/' + thisrecordid, headers=headers)
    print(deldns)


