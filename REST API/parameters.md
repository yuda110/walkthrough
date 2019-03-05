# REST API Parameters 종류 및 개요
참고: https://idratherbewriting.com/learnapidoc/docapis_doc_parameters.html


파라미터에는 4가지 타입이 있다.
- header parameters: 리퀘스트 헤더에 포함된 파라미터. 보통 권한 부여(권한 부여)에 관련되어 있다.
- path parameters: 엔드포인트에서 쿼리문(?) 이전에 있는 파라미터. 보통 중괄호({}) 안에 있다.
- query string parameters: 쿼리문 내의 파라미터. 엔드포인트에서 ? 뒤에 있다.
- request body parameters: 리퀘스트 본문에 포함된 파라미터. 보통 JSON 형식으로 제출된다.

### header parameters
헤더 파라미터는 보통 인증(Authentication)과 권한 부여(authorization) 두 가지 목적으로 사용된다. 
- 인증: 정확한 identity 제공
- 허가: 특정 action 허용

#### 왜 필요한가?
read-only API의 경우엔 키가 필요 없는 경우도 있다. 하지만 대부분의 상업용 API의 경우 API 키나 다른 메서드를 통한 허가를 필요로 한다. 
만약 이런 보안이 없다면, 유저들은 별다른 등록 없이 API를 무제한으로 콜할 수 있을 것이고 이는 곧 수익 창출 문제를 야기한다.
또한 인증 절차가 없다면 유저 데이터를 가져올 때 어려움을 겪게 될 것이고, 악의적인 유저로부터 타 유저의 데이터를 보호할 수 없다. 
그리고 누가 나의 API를 사용하는지 혹은 어떤 엔드포인트가 가장 자주 사용되는지 알 수 없게 된다. 
즉 API 개발자는 반드시 API를 만들 때 인증과 허가에 대한 방안을 생각해두어야 한다.

#### 권한 부여(authorization)의 종류
- API Key
> {"api-key": "012asfaawe2342ljsfsndsdfaaabbb"}

대부분의 API들은 API 키를 요구한다. API 키는 리퀘스트 URL이나 리퀘스트 헤더에 포함되는 긴 문자열이다. API 키는 보통 API를 사용하는 사람을 식별하는 역할을 한다. 
키의 종류에는 public 키와 private 키가 있다. public 키는 보통 리퀘스트에 포함되는 반면, private 키는 패스워드와 같아 서버와 서버간의 통신에서만 사용된다.
	
- Basic Auth
	예) Authorization: Basic bG9sOnNlY3VyZQ==
	리퀘스트 헤더에 username:password 를 넣어 인증하는 방식이다. username과 password는 Base64로 인코딩된다. 
	Basic Auth를 사용하는 API는 HTTPS를 사용하는데, 이는 즉 주고 받는 메시지가 HTTP 프로토콜 내에서 암호화된다는 뜻이다. (HTTPS가 없다면 username과 password가 쉽게 디코드될 것이다.)
	API 서버가 메시지를 받을 때, 메시지를 복호화하며 헤더를 읽어낸다. 문자열을 디코딩하고 username과 password를 분석한 후 리퀘스트를 받아들일 것인지 거절할 것인지 결정한다.
	
	(Postman에서는 Authorization 탭에서 Basic Auth를 선택해 Basic Authorization을 정의할 수 있다.)
	
- HMAC(Hash-based message authorization code)
	해쉬 기반의 메시지 인증 코드를 전달하는 HMAC는 강화된 인증 방식으로 금융 관련 API에 주로 사용되는 헤더이다. 과정을 설명하자면,
	
	1) 서버와 클라이언트만이 알고 있는 secret 키를 사용해 메시지(예를 들어 리퀘스트 타임스탬프와 account ID)를 인코드한다. 
	2) 그리고 이것이 SHA(secure hashing algorithm)로 해쉬되면 우리가 흔히 말하는 '서명(signature)'이라는 것이 나오는데 이 서명이 리퀘스트 헤더에 자리하게 된다.
	3) 클라이언트는 이 서명과 원본 메시지를 함께 서버에 보낸다.
	4) 서버가 요청을 받으면, 서버는 클라이언트가 했던 것과 똑같이 원본 메시지와 secret 키를 조합해 SHA 알고리즘으로 서명을 만든다.
	5) 이 서명과 서버가 가진 서명을 비교하여 일치하는지 확인한다.
	
- OAuth 2.0
	OAuth 2.0은 다른 인증 서버를 통해 API 서버에 접근할 수 있는 권한을 부여하는 방법이다. 쉽게 말해 '구글로 로그인하기', '페이스북으로 로그인하기' 등을 떠올리면 된다. 참고로 OAuth 1.0 '프로토콜'은 인증만, OAuth 2.0 '프레임워크'는 인증과 권한 부여를 모두 할 수 있다.
	
	- one-legged OAuth: 민감한 정보를 가지고 있지 않으며 기본적이거나 read-only 정보만 제공할 경우 사용
	- three-legged OAuth: 
		민감한 정보를 가지고 있어 이를 보호할 필요가 있을 경우. 이때 인증 서버와 API 서버 그리고 유저(앱) 세 그룹이 엮이게 된다.
		1) 유저가 사용하는 앱에서 application 키와 secret 키를 인증 서버의 로그인 페이지에 보낸다. 인증되었다면, 인증 서버가 유저에게 엑세스 토큰을 보낸다.
		2) 엑세스 토큰은  쿼리 파라미터에 패키징된다.
