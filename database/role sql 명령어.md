# SQL 명령어와 psql

### ROLE

ROLE은 CREATE ROLE 권한을 가진 유저에 의해 생성된다.

**롤 생성**

    CREATE ROLE role_name;

**로그인 기능이 있는 롤 생성**

    CREATE ROLE role_name WITH LOGIN;

**기존 롤에 로그인 기능 추가**
    
    ALTER ROLE role_name WITH LOGIN;

**롤 삭제**

    DROP ROLE role_name;

**데이터베이스에 대한 권한 부여**

    GRANT ALL ON DATABASE database_name TO role_name;
    GRANT CREATE_DB

**유저(혹은 또다른 ROLE)에게 ROLE 부여**
    
    GRANT role_name TO user_name;

<br>

### 참고
[psql cheatsheet](https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546)
