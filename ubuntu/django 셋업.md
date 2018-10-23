# django 셋업


### 파이썬 설치
- 프로젝트들 다 clone한 뒤, python과 pip을 받아줌

        $ sudo apt-get install python3
        $ sudo apt-get install python3-setuptools
        $ sudo apt-get update

- 서버를 다시 연 뒤,

        $ sudo apt-get install python3-pip
        $ sudo -H pip3 install --upgrade pip
    
- virtualenv 설치 

        $ sudo -H pip3 install virtualenv
        $ sudo -H virtualenv venv/{{project-env-name}}
        $ source /home/venv/{{project-env-name}}/bin/activate

- requirements 받기

        $ sudo pip install -r requirements.txt
    
    
    
### 발생가능한 오류 핸들링
- mysql_config not found 오류나면,

        $ sudo apt-get install libmysqlclient-dev
        $ sudo apt-get update

- unable to execute 'x86_64-linux-gnu-gcc' <<< 이런 오류나면
    
        $ sudo apt-get install gcc


### 마지막으로 migrate
    $ python3 manage.py migrate