# CrawlingAPI 개요
 이 폴더에 있는 Python 소스는 BeautifulSoup 라이브러리를 이용하여
Baekjoon(문제 정보, 우리 학교 학생이 푼 문제 정보 등)과 solved.ac(문제의 난이도)를 크롤링하는 함수를 제공하는 API 입니다. API를 사용하기 위해 import 하여야 하는 파일은 CrawlingAPI.py이며 그 외 파일은 함수를 디버그하거나, CrawlingAPI.py를 구현하기위해 사용됩니다.

# API에 포함되는 함수가 return 할 JSON에서의 객체 구조
 API 내 함수는 크게, 반환할 때 Python 객체(주로 리스트)를 반환하는 함수와 JSON의 문법을 따르는 string을 반환하는 함수로 나뉩니다. 일부는 아래와 같은 형식을 따릅니다.
 
## Baekjoon 문제
 Baekjoon 문제에 대한 정보를 JSON으로 반환할 때는 아래와 같은 형식을 따릅니다.
 
<pre><code>
{
	"id": 문제 번호 (문자열),
	"title": 문제 제목 (문자열),
	"rank": solved.ac 기준 티어, 아래 설명 참조
	"solver_count": 맞은 사람의 수 (문자열이며, 맞았습니다!!의 수가 아님),
	"ac_rate": 정답 비율 (0~100 까지의 실수를 나타내는 문자열)
}
</code></pre>

## JSON에서 Solved.ac의 문제 티어 표현 방법
 Solved.ac에서 문제의 티어는 Bronze, Silver, Gold, Platinum, Diamond, Ruby, Unrated, 번외로 나눕니다. 티어는 문자열로 아래와 같이 표현합니다.
 
 1. Bronze 5 ~ Bronze 1 : "B5", "B4", ..., "B1"
 2. Silver 5 ~ Silver 1 : "S5", "S4", ..., "S1"
 3. Gold 5 ~ Gold 1 : "G5", "G4", ..., "G1"
 4. Platinum 5 ~ Platinum 1 : "P5", "P4", ..., "P1"
 5. Diamond 5 ~ Diamond 1 : "D5", "D4", ..., "D1"
 6. Ruby 5 ~ Ruby 1 : "R5", "R4", ..., "R1"
 7. Unrated : "U"
 8. 번외 : "N"

# API에 구현되는 함수 목록
## (string) getAllProb_JSON()
백준에 존재하는 모든 문제 목록을 JSON 형식의 문자열로 반환합니다.

<pre><code>
ex. 아래 내용을 담은 문자열
[
	{
		"id": "1000",
		"title": "A+B",
		"rank": "B5",
		"solver_count": "84016",
		"ac_rate": "44.931"
	},
	{
		... # 위의 예시와 같은 형식의 다음 문제 내용
	},
	 ... # 그 외 모든 문제
]
</code></pre>

## (int list) getUOSProbList()
우리학교에서 푼 문제의 ID(정수)를 담은 리스트를 반환합니다.

<pre><code>ex. [ 1000, 1001, 1002, ..., 99999 ]</code></pre>

## (string) getUOSProbList_JSON()
위의 getUOSProblemsList()과 목적은 같지만 반환 형식이 JSON 형식의 문자열입니다.

<pre><code>ex. 다음 내용을 담은 문자열 : [ 1000, 1001, 1002, ..., 99999 ]</code></pre>

## (int) getLastSubID()
백준 채점 시스템에서의 마지막 제출번호를 반환 (단, "채점중", "기다리는중"인 제출은 제외하여 생각)

<pre><code>ex. 18542883</code></pre>

## (int) getLastProbID()
백준 문제 목록에서의 마지막 문제의 번호를 반환합니다.

<pre><code>ex. 18807</code></pre>

## (int list) getSolvedAfter((int) subID)
지난 마지막 제출번호(subID) 이후에 우리학교에서 제출하여 "맞았습니다!!"를 받은 문제의 리스트를 반환합니다. (중복 없음)

<pre><code>ex. [ 1234, 9876, ..., 5678 ]</code></pre>

## (string) getSolvedAfter_JSON((int) subID)
위의 getSolvedAfter((int) subID)와 목적은 같지만 반환 형식이 JSON 형식의 문자열입니다.

<pre><code>ex. 다음 내용을 담은 문자열 : [ 1234, 9876, ..., 5678 ]</code></pre>

## (string) getProbsAfter_JSON((int) probID)
지난 마지막 문제 번호(probID) 이후에 새로 추가된 문제 목록을 JSON 형식으로 반환합니다.

<pre><code>
[
	{
		"id": "18801",
		"title": "댐",
		"rank": "R5",
		"solver_count": "21",
		"ac_rate": "43.750"
	},
	{
		... # 위의 예시와 같은 형식의 다음 문제 내용
	},
	 ... # 그 외 추가된 모든 문제
]
</code></pre>

## (string) getProbInfo((int) id)
id에 해당하는 문제의 정보를 새로 가져옵니다.

<pre><code>
ex. 아래 내용을 담은 문자열 (getProbInfo(18801))
{
	"id": 18801,
	"title": "댐",
	"rank": "R5",
	"solver_count": 21,
	"ac_rate": 43.750
}
</code></pre>
