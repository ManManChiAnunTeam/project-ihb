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


def getProbsInPage(page):
    probs = []
    html = urlopen(PROBLEMSET_URL + str(page))
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
        found = getProbsInPage(page)
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


def getSolved(top):
    # not implemented
    html = None
    if top is None:
        html = urlopen(STATUS_URL)
    else:
        html = urlopen(STATUS_URL + "&top=" + top)
    bs = BeautifulSoup(html, "lxml")
    pass


def getSolvedAfter(subID):
    pass