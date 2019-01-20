# Jekyll로 GitHub 블로그 만들기

### jekyll 프로젝트 생성
일단 컴퓨터에 루비가 있는지 확인한 뒤,

    $ ruby -v
    
없다면 루비를 설치한다.
윈도우의 경우, [인스톨러](https://rubyinstaller.org/downloads/)를 이용해 설치한다.

> 루비란 스크립트 언어이자 순수 객체지향 프로그래밍 언어이다. 루비에서는 젬(gem)을 통해 폭넓은 서드파티 라이브러리를 제공한다. 
**RubyGems**는 루비에 특화된 `apt-get`과 비슷한 분산 패키지 시스템으로, 라이브러리 작성이나 공개, 설치 등을 도와주는 시스템이다.
루비 1.9 이후 버전부터는 루비에 동봉되어 있어 따로 설치할 필요가 없다.

그럼 이제 `gem`으로 jekyll 라이브러리를 설치하자.

    $ gem install jekyll
    
그리고 내 jekyll 사이트를 생성하자.

    $ jekyll new [site-name]
    
> 지킬 테마들은 대부분 오픈소스로 제공된다.
특정 테마를 적용하고 싶다면 위처럼 `jekyll new [site-name]` 명령어를 사용할 필요 없이 해당 테마 폴더를 그대로 복사+붙여넣기 하면 된다.

### dependency 설치

먼저 `bundler`를 설치해야 한다. 
`bundler`는 필요한 gem과 버전을 추적하고 설치하여 루비 프로젝트를 위한 일관된 환경을 제공한다.

    $ gem install bundler

> bundler를 설치할 때 주의해야 할 점은, `Gemfile.lock`에 기재되어 있는 **BUNDLED WITH**의 버전과 같아야 한다는 것이다.
이 버전을 맞추지 않으면 **GemNotFoundException** 에러가 발생할 수 있다. 
특정 버전을 설치할 때엔 `gem install bundler -v [version]` 명령어를 사용한다.
    
그 후 bundle 명령어를 사용해 필요한 gem을 설치한다.

    $ bundle install

이제 다음 명령어로 jekyll을 실행한다.

    $ jekyll serve 
    
http://localhost:4000에 접속하면 내 사이트가 보인다.
블로그 타이틀, 카테고리, 경로 등을 변경하고 싶다면 `_config.yml` 파일을 적당히 수정한다.

### admin 페이지 추가
프로젝트 폴더 내의 `Gemfile` 아래 다음을 추가해준다.
http://localhost:4000/admin으로 접속하여 관리자 페이지에 들어갈 수 있다.

    gem 'jekyll-admin', group: :jekyll_plugins
    