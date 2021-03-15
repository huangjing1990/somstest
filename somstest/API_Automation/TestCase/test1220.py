import requests
# requests.packages.urllib3.disable_warnings()
#
# url="https://backstageservices.dreawer.com/ecmps/getUserToken?appId=1514e1d61686438f95fa46f19070c126"
# header ={"Authorization":"94a58ede78564cf78f9ebde33e4c85f2","appid":"1514e1d61686438f95fa46f19070c126"}
# r = requests.get(url,headers = header,verify=False)
#
# print(r.text)


url = "https://backstageservices.dreawer.com/ecmps/login"
header = {"Content-Type": "application/json"}
data = {"phoneNumber": "15527060286", "password": "hbc23687"}
r = requests.post(url, json=data, headers=header)

print(r.text)
