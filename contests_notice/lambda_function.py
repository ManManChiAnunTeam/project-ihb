import requests, json, time
from bs4 import BeautifulSoup
from datetime import datetime

codeforces_url = "https://codeforces.com"
atcoder_url = "https://atcoder.jp"
slack_url = "https://hooks.slack.com/services/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"
channel_ID = {'Codeforces' : 'C0105GWQM28', 'Atcoder' : 'C01062ANCCD'}

def lambda_handler(event, context):

    # load upcoming contest data
    with open('upcoming_contests.json', 'r') as f:
        upcoming_contests_json = f.read()
        upcoming_contests = json.loads(upcoming_contests_json)
        prv_upcoming_contest_names = {contest['name'] for contest in upcoming_contests}

    next_upcoming_contests = []
    next_upcoming_contests += get_cf_upcoming_contests(prv_upcoming_contest_names)
    next_upcoming_contests += get_ac_upcoming_contests(prv_upcoming_contest_names)

    # notice today contests
    for upcoming_contest in next_upcoming_contests:
        if upcoming_contest['start_time'] - time.time() <= 12*60*60 + 600:
            notice_today_contest(upcoming_contest)

    # update upcoming contest data
    with open("upcoming_contests.json", 'w') as f:
        json.dump(next_upcoming_contests, f)

def get_cf_upcoming_contests(prv_upcoming_contest_names):
    global codeforces_url

    # request to codeforces api
    res = requests.get(codeforces_url + "/api/contest.list?gym=false").json()
    parse_contests = res['result']

    # parse codeforces
    ret = []
    for parse_contest in parse_contests:
        if parse_contest['phase'] != 'BEFORE': break
        contest = {}
        minute = parse_contest['durationSeconds'] // 60
        contest['id'] = parse_contest['id']
        contest['name'] = parse_contest['name']
        contest['start_time'] = parse_contest['startTimeSeconds'] + (9 * 60 * 60)
        contest['duration'] = f'{minute // 60:02}:{minute % 60:02}'
        contest['url'] = codeforces_url + '/contests/' + str(contest['id'])
        contest['oj'] = 'Codeforces'

        # notice new contests
        if contest['name'] not in prv_upcoming_contest_names:
            notice_new_contest(contest)

        ret.append(contest)

    return ret

def get_ac_upcoming_contests(prv_upcoming_contest_names):
    global atcoder_url

    # request to atcoder
    res = requests.get(atcoder_url + '/contests')
    soup = BeautifulSoup(res.text, 'html.parser')
    upcoming_table = soup.find(id='contest-table-upcoming')
    upcoming_contests = upcoming_table.find_all("tr")[1:]

    # parse atcoder
    ret = []
    for upcoming_contest in upcoming_contests:
        contest = {}
        contest['id'] = None
        tds = upcoming_contest.find_all('td')
        name = tds[1].find('a')
        datetime_obj = datetime.strptime(tds[0].text.split('+')[0], '%Y-%m-%d %H:%M:%S')
        contest['name'] = name.text
        contest['start_time'] = time.mktime(datetime_obj.timetuple())
        contest['duration'] = tds[2].text
        contest['url'] = atcoder_url + name['href']
        contest['oj'] = 'Atcoder'

        # notice new contests
        if contest['name'] not in prv_upcoming_contest_names:
            notice_new_contest(contest)

        ret.append(contest)

    return ret

def notice_new_contest(contest):
    global slack_url

    content = str(datetime.fromtimestamp(contest['start_time'])) + ' | '
    content += contest['duration'] + '\n'
    content += contest['url']

    payloads = {
        "attachments": [
            {
                "fallback" : "새로운 콘테스트가 생겼어요.",
                "pretext": "새로운 콘테스트가 생겼어요.",
                "color": "#000000",
                "fields": [{
                    "title": contest['name'],
                    "value": content,
                    "short": False
                }]
            }]
    }
    response = requests.post(
        slack_url, data=json.dumps(payloads),
        headers={'Content-Type': 'application/json'}
    )

def notice_today_contest(contest):
    global slack_url, channel_ID

    title = f"오늘 {contest['oj']} Contest가 개최됩니다!"
    content = contest['name'] + '\n'
    content += str(datetime.fromtimestamp(contest['start_time'])) + ' | '
    content += contest['duration'] + '\n'
    content += f"참가 등록 >> {contest['url']} <<\n\n"
    content += f"대회가 끝나고 궁금한게 있으면 <#{channel_ID[contest['oj']]}> 채널로 오세요."

    payloads = {
        "attachments": [
            {
                "fallback" : "12시간 후 콘테스트가 개최됩니다.",
                "pretext": "12시간 후 콘테스트가 개최됩니다.",
                "color": "#000000",
                "fields": [{
                    "title": title,
                    "value": content,
                    "short": False
                }]
            }]
    }
    response = requests.post(
        slack_url, data=json.dumps(payloads),
        headers={'Content-Type': 'application/json'}
    )
