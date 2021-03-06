import os, sys, urllib, urllib2, json

api_version_url = 'https://ddragon.leagueoflegends.com/api/versions.json'
realm_version_url = 'https://ddragon.leagueoflegends.com/realms/br.json'

def loadJsonFromUrl(url):
	r = urllib2.urlopen(url)
	str_r = r.read().decode('utf-8')
	return json.loads(str_r)

print 'Latest API Version: ' + loadJsonFromUrl(api_version_url)[0]

obj = loadJsonFromUrl(realm_version_url)

champs_vers = obj['n']['champion']

base_url = 'http://ddragon.leagueoflegends.com/cdn/'
champs_url = '%s%s/data/en_US/championFull.json' % (base_url, champs_vers)

print '\nRealm: BR'

print 'Champions: ' + champs_vers

obj = loadJsonFromUrl(champs_url)

output = []

for ck, champion in sorted(obj['data'].items()):
    skins = []

    for skin in champion['skins']:
        skins.append({'Id': int(skin['id']), 'Name': skin['name'], 'Num': skin['num'], 'ChampionId': int(champion['key'])})

    output.append({'Id': int(champion['key']), 'Name': champion['id'], 'DisplayName': champion['name'], 'Skins': skins})

    print(champion['name'])


with open('Champions.json', 'w') as f:
	json.dump(output, f)

with open('Champions.Version', 'w') as f:
	f.write(champs_vers)

output = []
