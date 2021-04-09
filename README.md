# git 
## 로컬 컴퓨터 git 설치 : https://git-scm.com/
## 로컬 컴퓨터 
### 로컬 컴퓨터 환경 설정
+ git config --global user.email "you@example.com"
+ git config --global user.name "Your Name“
### git 로컬 저장소 만들기 
<p>
<strong>1. 로컬 컴퓨터 작업 디렉토리 생성 </strong>
</p>
<p>
<strong>2. 로컬 컴퓨터 버전 관리 초기화 : git init </strong>
   + 생성된 작업 디렉토리로 이동하여 명령실행
   + git 디렉토리 용어
     + 작업트리(working tree) : 파일을 수정, 저장 등의 작업을 진행하는 디렉토리
     + 스테이지(stage) : .git 디렉토리에 위치하며 버전으로 만들 파일이 대기하는 디렉토리
     + 저장소(repository) : .git 디렉토리에 위치하며스테이지에서 대기하고 있던 파일들을 버전으로 만들어 저장하는 디렉토리
 </p>
<p>
 <strong>3. 로컬 컴퓨터 파일 버전 관리</strong><br>
   + git add 파일명 :작업트리 파일 생성 -> git commit -m "메시지" : 스테이지로 이동(스테이징) -> 저장소로 올리기
   + git commit -am "메시지" : 스테이징과 저장소 커밋 동시에 실시
   + git status : 현재 상태 확인
   + git log : 버전확인 
<strong>4. 변경사항확인</strong><br>
   + 수정한 파일과 최종본과의 차이 확인 : git diff
     + git status 로 확인했을 때  modify인 경우 확인
<strong>5.파일 되돌리기</strong><br>
   + 스테이징 되기 전에 파일을 수정한 경우 최신 파일로 되돌리기  : git checkout -- 파일명
   + 스테이징된 파일 되돌리기 : git restore --staged 파일명
   + 최신 커밋된 파일 되돌리기 : git reset HEAD~n 
     + n 번째 최신 커밋 취소
     + git reset —hard 복사한 커밋 해시
