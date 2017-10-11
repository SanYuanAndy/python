#coding=utf8
import json
import os

def load(data):
    with open(data, 'r') as f:
        sJson = f.read()
        #print sJson
        jsonObj = json.loads(sJson)
        return jsonObj

#结果存储到results中，results类型为map
def parse(sFile, results):
    print sFile
    jsonArray = load(sFile)
    for jsonObj in jsonArray:
        sName = jsonObj['name']
        sWord = jsonObj['word']
        score = jsonObj['score']
        sResult = '%s  %5s  %f'%(sName, sWord, score)
        #print sResult
        obj = {}
        if not results.has_key(sName):
            results[sName] = obj
            
        obj = results[sName]
        obj['word'] = sWord
        if sFile.startswith('v2'):
            scores = []
            key = 'v2'
            if not obj.has_key(key):
                obj[key] = scores
            scores = obj[key]
            scores.append(score)
        elif sFile.startswith('v3'):
            scores = []
            key = 'v3'
            if not obj.has_key(key):
                obj[key] = scores
            scores = obj[key]
            scores.append(score)
    print
    print

#结果存储到results中，results类型为map
def parses(results):
    dirs = os.listdir('.')
    for child in dirs:
        if os.path.isdir(child) and (child == 'v2' or child == 'v3'):
            jsonFiles = os.listdir(child)
            for f in jsonFiles:
                if f.endswith('.json'):
                    path = "%s/%s"%(child, f)
                    parse(path, results)
           
results_map = {}
parses(results_map)

result_keys = results_map.keys()
for result in result_keys:
    jsonObj = results_map[result]
    sWord = jsonObj['word']
    sName = result
    score_v2 = ''
    score_v3 = ''
    if jsonObj.has_key('v2'):
        scores = jsonObj['v2']
        for score in scores:
            sScore = "%f"%(score)
            index = sScore.find('.')
            if index != -1:
                sScore = sScore[0:index + 4]
            score_v2 = '%s %s '%(score_v2, sScore)
            
    if jsonObj.has_key('v3'):
        scores = jsonObj['v3']
        scores = jsonObj['v3']
        for score in scores:
            sScore = "%f"%(score)
            index = sScore.find('.')
            if index != -1:
                sScore = sScore[0:index + 4]
            score_v3 = '%s %s '%(score_v3, sScore)
        
    sResult = '%s  %5s  %s %s'%(sName, sWord, score_v3, score_v2)
    print sResult
