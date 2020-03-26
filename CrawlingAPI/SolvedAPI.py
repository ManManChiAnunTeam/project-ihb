from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import random

SOLVED_TIER = "https://solved.ac/search/solved%3A0..?page="
TIER_CHAR = ['B', 'S', 'G', 'P', 'D', 'R']


def TierNumToStr(numStr):
    if numStr == "nr":
        return "N"

    num = int(numStr)
    if num == 0:
        return "U"

    return TIER_CHAR[(num - 1) // 5] + str(5 - (num - 1) % 5)


def getProbsInPage(page):
    probs = []
    html = urlopen(SOLVED_TIER + str(page))
    bs = BeautifulSoup(html, "lxml")
    pSet = bs.find("tbody").find_all(class_="problem_id")

    for prob in pSet:
        pId = prob.getText().strip()
        src = prob.find("img")["src"]
        tier = TierNumToStr(src[src.rfind('/') + 1:src.rfind('.')])
        probMap = {"id":pId, "rank":tier}
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