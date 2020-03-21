from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import random

SLEEP_RANGE = (1, 3)


class ProbInfo:
    def __init__(self, id, rate, solvers):
        self.ID = id
        self.Rate = rate
        self.Solvers = solvers

    def __str__(self):
        return "ID: " + str(self.ID) + ", Rate: " + str(self.Rate) + ", Solvers: " + str(self.Solvers)

    def __repr__(self):
        return self.__str__()


def getProbsInPage(page):
    probs = []
    html = urlopen("https://www.acmicpc.net/problemset/" + str(page))
    bs = BeautifulSoup(html, "html.parser")
    pSet = bs.find(id="problemset").find_all("tr")
    pCount = 0

    for prob in pSet:
        info = prob.find_all("td")
        if len(info) == 0:
            continue
        pCount += 1
        probs.append(ProbInfo(info[0].getText(), info[-1].getText(), info[-3].getText()))

    return probs


def getAllProbs():
    probs = []
    page = 1
    while True:
        print(str(page) + "쪽 가져오는 중...")
        found = getProbsInPage(page)
        if len(found) == 0:
            break
        probs += found
        page += 1
        #time.sleep(random.uniform(*SLEEP_RANGE))
    return probs


for prob in getAllProbs():
    print(prob)

