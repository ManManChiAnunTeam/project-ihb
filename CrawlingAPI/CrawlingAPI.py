import BaekjoonAPI as bapi
import SolvedAPI as sapi
import json


def searchID(id, pList):
    start = 0
    end = len(pList) - 1

    while start <= end:
        mid = (start + end) // 2
        if pList[mid]["id"] == id:
            return mid
        elif int(pList[mid]["id"]) < int(id):
            start = mid + 1
        else:
            end = mid - 1

    return None


'''def toJSON(item):
    if isinstance(item, dict):
        return json.dumps(item)

    elif isinstance(item, list):
        result = "[ "
        for i in range(0, len(item)):
            result += toJSON(item[i])
            if i != len(item) - 1:
                result += ", "
        result += " ]"
        return result

    else:
        return "\"" + str(item) + "\""'''


def getAllProbs():
    solvedList = sapi.getAllProbs()
    baekList = bapi.getAllProbs()

    for prob in solvedList:
        index = searchID(prob["id"], baekList)
        if index is not None:
            baekList[index]["rank"] = prob["rank"]

    return baekList


# 백준에 존재하는 모든 문제 목록을 JSON 형식의 문자열로 반환합니다.
def getAllProb_JSON():
    return json.dumps(getAllProbs())


# 우리학교에서 푼 문제의 ID(문자열)를 담은 리스트를 반환합니다.
def getUOSProbList():
    solved = set()
    for mem in bapi.getUOSMembers():
        solved.update(bapi.getSolvedList(mem))
    return list(solved)


# 위의 getUOSProblemsList()과 목적은 같지만 반환 형식이 JSON 형식의 문자열입니다.
def getUOSProbList_JSON():
    return json.dumps(getUOSProbList())


# 백준 채점 시스템에서 "맞았습니다!!"를 받은 우리학교의 마지막 제출번호를 반환합니다.
def getLastSubID():
    return bapi.getLastSubID()


# 백준 문제 목록에서의 마지막 문제의 번호를 반환합니다.
def getLastProbID():
    return bapi.getLastProbID()


# 지난 마지막 제출번호(subID) 이후에 우리학교에서 제출하여 "맞았습니다!!"를 받은 문제의 리스트를 반환합니다. (중복 없음)
def getSolvedAfter(subID):
    return list(bapi.getSolvedAfter(subID))


# 위의 getSolvedAfter((string) subID)와 목적은 같지만 반환 형식이 JSON 형식의 문자열입니다.
def getSolvedAfter_JSON(subID):
    return json.dumps(getSolvedAfter(subID))


# 지난 마지막 문제 번호(probID) 이후에 새로 추가된 문제 목록을 dictionary를 원소로 하는 리스트 형식으로 반환합니다.
# (백준의 "추가된 문제", "추가된 영어 문제"에서 조회하므로, 너무 오래전의 문제 번호를 입력하면 문제를 모두 조회하지 못할 수 있습니다.)
def getProbsAfter(probID):
    baekList = bapi.getProbsAfter(probID)
    solvedList = sapi.getAllProbs()
    baekList.sort(key=lambda x: int(x["id"]))

    for prob in solvedList:
        index = searchID(prob["id"], baekList)
        if index is not None:
            baekList[index]["rank"] = prob["rank"]

    return baekList


# 위의 getProbsAfter((string) probID)와 목적은 같지만 반환 형식이 JSON 형식의 문자열입니다.
def getProbsAfter_JSON(probID):
    return json.dumps(getProbsAfter(probID))
