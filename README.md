# git 
## 로컬 컴퓨터 git 설치 : https://git-scm.com/
## 로컬 컴퓨터 
### 로컬 컴퓨터 환경 설정
+ git config --global user.email "you@example.com"
+ git config --global user.name "Your Name“
### git 로컬 저장소 만들기 
1. 로컬 컴퓨터 작업 디렉토리 생성 
2. 로컬 컴퓨터 버전 관리 초기화 : git init
   + 생성된 작업 디렉토리로 이동하여 명령실행
   + git 디렉토리 용어
    - 작업트리(working tree) : 파일을 수정, 저장 등의 작업을 진행하는 디렉토리
    - 스테이지(stage) : .git 디렉토리에 위치하며 버전으로 만들 파일이 대기하는 디렉토리
    - 저장소(repository) : .git 디렉토리에 위치하며스테이지에서 대기하고 있던 파일들을 버전으로 만들어 저장하는 디렉토리
