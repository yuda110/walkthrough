# Webstorm built-in server 사용하기

- c:\Windows\System32\drivers\etc hosts 파일에서 다음 추가

        127.0.0.1	[project-name]


- _setting > Build, Execution, Deployment > Debugger_ 에서 built-in server 항목 port를 **8090**으로 변경


- Webstorm 오른쪽 상단 _Run/Debug Configurations_ 에서 URL을 다음으로 변경

        http://project-name:8090/index.html
        

- html 문서 디렉토리가 `html/index.html` 이런 식이라면, html 폴더를 Resource Root로 변경
        