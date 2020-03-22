1. 초기 upcoming_contests.json 파일은 빈 json 파일. 실행하면 json파일이 업데이트 된다.

2. 외부 라이브러리(requests, bs4)는 AWS내에서 Layer로 넣어야한다. 첨부된 pack.zip을 업로드하면 됨.

3. DB 불러오기 / DB 저장하기 부분만 수정하면 끝

4. 실행시간은 3초를 조금 넘김

5. 추가로는 API를 이용해서 슬랙에 메세지를 입력하면 현재 upcoming 콘테스트 목록을 불러오도록 구현할 예정
