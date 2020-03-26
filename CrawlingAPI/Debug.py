import SolvedAPI as sapi
import BaekjoonAPI as bapi
import CrawlingAPI as capi
import time


if __name__=="__main__":
    start = time.time()

    # print(capi.toJSON(bapi.getUOSMembers()))

    '''con = set()
    con.update(bapi.getSolvedList("powergee"))
    print(con)
    print(len(con))'''

    # print(capi.getUOSProbList_JSON())

    # print(capi.getLastSubID())

    print(capi.getLastProbID())

    print(str(time.time() - start) + "초 실행")