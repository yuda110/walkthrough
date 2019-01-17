# 인포뱅크 문자 전송 API 사용방법

참고: https://www.ibizplus.co.kr/technical/datacenter/rest#api03

- REST API를 사용합니다.

### API 리스트
- **인증(토큰 발급) API**: 서비스 이용시 인증에 사용할 토큰을 발급받음(24시간 만료)
- **메시지 전송 API**: 메시지 발송을 요청함

### API 상세
#### 인증(토큰 발급) API
다음 정보를 이용하여 API를 호출할 수 있는 토큰을 발급 받을 수 있음
- X-IB-Client-Id : 인포뱅크를 통해 발급받은 ID
- X-IB-Client-Passwd : 인포뱅크를 통해 발급받은 Password

[Request]

    method : POST 
    path : /auth/v3/token
    header 
        - Accept : application/json
        - X-IB-Client-Id : ID
        - X-IB-Client-Passwd : Password
    
    
#### 메시지 전송 API
- 1개의 메시지를 최대 200개의 수신번호로 발송 가능하며, 수신번호 별 치환 문구는 5개까지 사용 가능

[Request]

    method : POST 
    path : /auth/v3/multiple-destinations
    header 
        - Accept : application/json
        - X-IB-Client-Id : ID
        - X-IB-Client-Passwd : Password
    body
        다양함
        
