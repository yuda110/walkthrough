# ubuntu에서 pycharm/webstorm 설치하기

[여기서](https://www.jetbrains.com/pycharm/download/#section=linux) pycharm tar 파일 다운로드 한 뒤,

- 다운로드 폴더 가서 압축풀고,


    $ sudo tar -zxvf pycharm-professional-2017.2.1.tar.gz -C /opt
    
    
- 이 폴더를 적당한 장소로 옮기고
    
    
    $ sudo mv pycharm-professional-2017.2.1 pycharm
    
    
- `pycharm/bin` 디렉토리로 가서 pycharm.sh 실행하면 pycharm 실행됨


    $ cd /opt/pycharm/bin
    $ ./pycharm.sh


> 매번 pycharm.sh로 실행하기 귀찮으니까 실행파일을 바탕화면에 만들어주는 게 좋다.