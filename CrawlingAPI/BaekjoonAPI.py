from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import random

PROBLEMSET_URL = "https://www.acmicpc.net/problemset/"
UOSRANK_URL = "https://www.acmicpc.net/school/ranklist/302/"
USER_URL = "https://www.acmicpc.net/user/"
STATUS_URL = "https://www.acmicpc.net/status?school_id=302&result_id=4"
NEWPROB_URL = "https://www.acmicpc.net/newproblems"
NEWPROBENG_URL = "https://www.acmicpc.net/newproblems/english"


def getProbsInPage(url):
    probs = []
    html = urlopen(url)
    bs = BeautifulSoup(html, "lxml")
    pSet = bs.find(id="problemset").find_all("tr")

    for prob in pSet:
        info = prob.find_all("td")
        if len(info) == 0:
            continue
        probMap = {"id":info[0].getText().strip(), "title":info[1].find("a").getText(), "rank":"U", "ac_rate":info[-1].getText(), "solver_count":info[-3].getText()}
        probs.append(probMap)

    return probs


def getAllProbs():
    probs = []
    page = 1
    while True:
        found = getProbsInPage(PROBLEMSET_URL + str(page))
        if len(found) == 0:
            break
        probs += found
        page += 1
    return probs


def getUOSMembersInPage(page):
    mems = []
    try:
        html = urlopen(UOSRANK_URL + str(page))
        bs = BeautifulSoup(html, "lxml")
        mList = bs.find(id="ranklist").find_all("tr")

        for mem in mList:
            info = mem.find_all("td")
            if len(info) == 0:
                continue
            mems.append(info[1].getText())
    except:
        pass

    return mems


def getUOSMembers():
    mems = []
    page = 1
    while True:
        found = getUOSMembersInPage(page)
        if len(found) == 0:
            break
        mems += found
        page += 1
    return mems


def getSolvedList(memID):
    probs = []
    html = urlopen(USER_URL + memID)
    bs = BeautifulSoup(html, "lxml")
    nums = bs.find(class_="panel-body").find_all(class_="problem_number")

    for num in nums:
        probs.append(num.find("a").getText())

    return probs


def getLastSubID():
    html = urlopen(STATUS_URL)
    bs = BeautifulSoup(html, "lxml")
    idStr = bs.find(id="status-table").find("tbody").find("tr")["id"]
    return idStr[idStr.rfind('-')+1 : ]


def getLastProbID():
    html = urlopen(NEWPROB_URL)
    bs = BeautifulSoup(html, "lxml")
    id1 = bs.find(id="problemset").find("tbody").find(class_="list_problem_id").getText()
    html = urlopen(NEWPROBENG_URL)
    bs = BeautifulSoup(html, "lxml")
    id2 = bs.find(id="problemset").find("tbody").find(class_="list_problem_id").getText()

    if int(id1) > int(id2):
        return id1
    else:
        return id2


# top(채점번호)부터 채점번호가 감소하는 방향으로 채점 현황의 한 페이지를 크롤링함.
# 반환값은 (Boolean: 페이지를 모두 크롤링 하였는지 여부, String: 크롤링 한 제출의 가장 마지막(번호가 가장 작은) 번호) 형식의 튜플이다.
# 반환 튜블의 Boolean에 대하여: 채점번호가 endOfSub 이하인 제출을 발견하면 크롤링을 중단하고 False를 반환한다. (그 외, True 반환)
def getSolved(top, resultSet, endOfSub=""):
    html = None
    if top is None:
        html = urlopen(STATUS_URL)
    else:
        html = urlopen(STATUS_URL + "&top=" + top)
    bs = BeautifulSoup(html, "lxml")
    subs = bs.find(id="status-table").find("tbody").find_all("tr")

    canReadMore = True
    minSub = None
    for sub in subs:
        info = sub.find_all("td")
        subID = info[0].getText()
        if subID == endOfSub:
            canReadMore = False
            break
        resultSet.add(info[2].find("a").getText())
        minSub = subID

    return (canReadMore, minSub)


def getSolvedAfter(subID):
    result = set()
    top = getLastSubID()

    while True:
        readAll, minSub = getSolved(top, result, subID)
        if not readAll:
            break
        top = minSub

    return result


def getProbsAfter(probID):
    result = []
    probID_int = int(probID)
    result += [prob for prob in getProbsInPage(NEWPROB_URL) if int(prob["id"]) > probID_int]
    result += [prob for prob in getProbsInPage(NEWPROBENG_URL) if int(prob["id"]) > probID_int]
    return result
