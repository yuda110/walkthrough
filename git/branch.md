
# branch


* branch 존재 이유를 파악하고 쓰자. 
* 충돌 피하기 위함뿐만 아니라 git이 '분산 버전 관리 시스템'이라는 것을 기억하자.


### 리스트
> 모든

    $ git branch -a
    
> remote

    $ git branch -r
    
> 모든 브랜치 및 커밋 상태

    $ git branch -v -a


### 원격저장소 branch 가져올 때

    $ git checkout -b 생성할브랜치이름 원격브랜치이름
    (ex. git checkout -b test origin/test)


### 다른 branch에서 특정 파일만 pull하고 싶을 때

    $ git checkout test
    $ git checkout --patch sass index.html
  
> test 브랜치에 index.html 이 이미 존재하는 경우

    $ git checkout sass index.html
    

### branch 삭제

> 일단 fetch

    $ git fetch --prune origin
    $ git fetch -p origin

> delete local branch

    $ git branch -d <branch_name>
    $ git branch -D <branch_name>

> delete remote branch

    $ git push <remote_name> : <branch_name>
    (ex. git push origin :pyshell)
