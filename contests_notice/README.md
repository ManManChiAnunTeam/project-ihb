초기 upcoming_contests.json 파일은 빈 json 파일. 실행하면 json파일이 업데이트 된다.
한번 실행 시 실행시간은 3초를 조금 넘김


남은 작업

1. 외부 라이브러리(requests, bs4)는 AWS 내에서 Layer로 넣어야한다. 첨부된 pack.zip을 업로드하면 됨.

2. lambda function은 DB 불러오기 / DB 저장하기 부분만 AWS 내에서 구현하면 끝. 나머지는 그대로 복사하면 됨

3. 테스트를 눌렀을 때 정상적으로 슬랙으로 메세지가 오면 Amazon CloudWatch Events으로 1시간마다 실행하도록 설정

4. 슬랙에서 Outgoing WebHooks를 이용해 AWS로 요청이 오면 notice_all_upcoming_contests()가 실행되도록 설정 (API를 만들면 됨)
