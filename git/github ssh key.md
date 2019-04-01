### ssh 공개키 있는지 확인
    $ cd ~/.ssh

* **id_rsa**는 개인키, **id_rsa.pub**은 공개키
* 만약 이들이 없거나 .ssh 디렉토리도 없다면 ssh key를 생성해야 함


### github ssh key 만들고 적용하기
    $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    $ eval “$(ssh-agent -s)”
    $ ssh-add ~/.ssh/id_rsa

### .ssh/id_rsa.pub 내용 복사 후, `github Settings > SSH and GPG keys`에 추가
    
