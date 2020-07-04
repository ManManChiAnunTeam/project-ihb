# contests_notice

![](https://github.com/iknoom/project-ihb/blob/master/contests_notice/contest_notice_example.PNG)

AWS Lambda의 cloudwatch를 활용한 WebHook

다음 두 가지 경우에 대해서 메세지가 담긴 json을 Slack의 Incoming WebHooks에 POST해준다.

1. 일정에 새롭게 추가된 Contest가 있을 경우(Codeforces, AtCoder)

2. 시작까지 12시간 이내로 남은 Contest가 있을 경우(Codeforces, AtCoder)


## 설명

* get_cf_upcoming_contests(prv_upcoming_contest_names) : Codeforces는 제공해주는 API를 활용해서 contests 일정을 갱신한다.

* get_ac_upcoming_contests(prv_upcoming_contest_names) : AtCoder는 직접 크롤링을 해서 contests 일정을 갱신한다.

* notice_new_contest(contest) : 1. 일정에 새롭게 추가된 Contest가 있을 경우 POST

* notice_today_contest(contest) : 2. 시작까지 12시간 이내로 남은 Contest가 있을 경우 POST

* 초기 upcoming_contests.json 파일은 빈 json 파일. 실행하면 json파일이 한번에 업데이트 된다.

* 한번 실행 시 실행시간은 3초를 조금 넘긴다.


## To do

* 슬랙에서 Outgoing WebHooks를 이용해 AWS로 요청이 오면 notice_all_upcoming_contests()가 실행되도록 설정 (API를 만들면 됨)

* 오류 수정 (idempotent??)
