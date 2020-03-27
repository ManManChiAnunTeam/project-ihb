import SolvedAPI as sapi
import BaekjoonAPI as bapi
import CrawlingAPI as capi
import time
import sys


if __name__=="__main__":
    # print(capi.toJSON(bapi.getUOSMembers()))

    '''con = set()
    con.update(bapi.getSolvedList("powergee"))
    print(con)
    print(len(con))'''

    # print(capi.getUOSProbList_JSON())

    # print(capi.getLastSubID())

    # print(capi.getLastProbID())

    '''probs = set()
    print(bapi.getSolved("18719530", probs, "18717698"))
    print(probs)

    print(capi.getSolvedAfter_JSON("18710092"))'''
    f = open("debugOutput.txt", 'w', encoding="utf-8")
    f.write("Started\n")

    start = time.time()
    f.write("[getAllProb_JSON()]\n")
    f.write(capi.getAllProb_JSON() + "\n")
    f.write(str(time.time() - start) + "초 실행\n\n")

    start = time.time()
    f.write("[getUOSProbList_JSON()]\n")
    f.write(capi.getUOSProbList_JSON() + "\n")
    f.write(str(time.time() - start) + "초 실행\n\n")

    start = time.time()
    f.write("[getLastSubID()]\n")
    f.write(capi.getLastSubID() + "\n")
    f.write(str(time.time() - start) + "초 실행\n\n")

    start = time.time()
    f.write("[getLastProbID()]\n")
    f.write(capi.getLastProbID() + "\n")
    f.write(str(time.time() - start) + "초 실행\n\n")

    start = time.time()
    f.write("[getSolvedAfter_JSON(\"18717367\")]\n")
    f.write(capi.getSolvedAfter_JSON("18717367") + "\n")
    f.write(str(time.time() - start) + "초 실행\n\n")

    start = time.time()
    f.write("[getProbsAfter_JSON(\"18801\")]\n")
    f.write(capi.getProbsAfter_JSON("18801") + "\n")
    f.write(str(time.time() - start) + "초 실행\n\n")
