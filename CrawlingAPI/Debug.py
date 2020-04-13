import SolvedAPI as sapi
import BaekjoonAPI as bapi
import CrawlingAPI as capi
import time
import sys
import json

rank_list = ['B5', 'B4', 'B3', 'B2', 'B1',
             'S5', 'S4', 'S3', 'S2', 'S1',
             'G5', 'G4', 'G3', 'G2', 'G1',
             'P5', 'P4', 'P3', 'P2', 'P1',
             'D5', 'D4', 'D3', 'D2', 'D1',
             'R5', 'R4', 'R3', 'R2', 'R1',
             'U', 'N']

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

    # 모든 문제의 정보 출력.
    # start_time = time.time()
    # with open('json/AllProbs.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(capi.getAllProbs(), json_file, ensure_ascii=False)
    # end_time = time.time()
    # print(f"모든 문제 정보 출력 : {end_time - start_time}초")

    # SolvedProbIDs.json 정렬
    # with open('json/SolvedProbIDs.json', 'r') as json_file:
    #     solved_probs = json.load(json_file)
    # solved_probs.sort(key=lambda x: int(x))
    # with open('json/SolvedProbIDs.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(solved_probs, json_file, ensure_ascii=False)

    # Make UnsolvedProbs.json
    # with open('json/AllProbs.json', 'r', encoding='utf-8') as json_file:
    #     all_probs = json.load(json_file)
    # with open('json/SolvedProbIDs.json', 'r') as json_file:
    #     solved_prob_ids = json.load(json_file)
    #
    # unsolved_probs = dict.fromkeys(rank_list)
    # for rank in unsolved_probs:
    #     unsolved_probs[rank] = []
    # i = 0
    # for prob in all_probs:
    #     if prob['id'] != solved_prob_ids[i]:
    #         unsolved_probs[prob['rank']].append(prob)
    #     else:
    #         i += 1
    #         if i == len(solved_prob_ids):
    #             break
    #
    # with open('json/UnsolvedProbs.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(unsolved_probs, json_file, ensure_ascii=False)
    #
    # for rank in unsolved_probs:
    #     print(rank, len(unsolved_probs[rank]))
