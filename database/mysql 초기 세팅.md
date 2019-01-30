# MySQL 초기 세팅

## 윈도우에서

### [MySQL Community Server](https://dev.mysql.com/downloads/mysql/) 설치
- **MySQL Server**와 **MySQL Workbench** 설치
- MySQL Server 설치 시 초기 세팅(비밀번호 설정, 유저 추가 등)

### MySQL Workbench에서 Connection 생성
- [튜토리얼](https://dev.mysql.com/doc/workbench/en/wb-getting-started-tutorial-create-connection.html) 참고
- 홈 화면에서 + 버튼 누른 뒤, Connection Name을 짓고 `Configure Server Management` 버튼 클릭

### User 생성
- User 추가하고 싶다면 루트 계정으로 연결한 뒤, 왼쪽 사이드바에서 `Users and Privileges` 클릭
- `Add Account` 클릭하여 이름, 비밀번호 등 설정. 이때 Authentication Type은 'Standard'로 한다.
- 위쪽 탭에서 Administrative Roles에서 역할을 정해준 뒤, `Apply` 버튼 클릭 

### Database 생성
- 탭에서 `New Schema` 버튼 클릭
- 이름 정해준 뒤, 