import json
jsonfile = open('learningJson.json',)
jsondata = json.load(jsonfile)
print(jsondata['education'][0]['subjects'][0])
#print(jsondata)
jsonfile.close()