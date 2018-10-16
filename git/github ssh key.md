### ssh 공개키 있는지 확인
    $ cd ~/.ssh

* **id_rsa**는 개인키, **id_rsa.pub**은 공개키
* 만약 이들이 없거나 .ssh 디렉토리도 없다면 ssh key를 생성해야 함


### github ssh key 만들고 적용하기
    $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    $ eval “$(ssh-agent -s)”
    $ ssh-add ~/.ssh/id_rsa

###github 설정 페이지 가서(내 프로필 설정 혹은 해당 프로젝트 페이지) SSH key 추가
    $ git clone git@github.com:[아이디 혹은 그룹]/[프로젝트명].git