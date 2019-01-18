# Jekyll

### 초기 세팅

    $ gem install jekyll
    $ jekyll new my-site
    $ cd my-site
    $ jekyll serve
    
위 설치가 끝난 뒤, http://localhost:4000에 접속하면 내 사이트가 보인다.

### 테마 적용
빈 폴더에 해당 테마 소스를 전부 복사+붙여넣기 한다.
`_config.yml` 파일을 적당히 수정해준다.

### admin 페이지 추가
프로젝트 폴더 내의 `Gemfile` 아래 다음을 추가해준다.
http://localhost:4000/admin으로 접속하여 관리자 페이지에 들어갈 수 있다.

    gem 'jekyll-admin', group: :jekyll_plugins
    
