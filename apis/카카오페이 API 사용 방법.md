# 카카오페이 API 사용 방법

0. 시작 전
- 웹사이트 도메인 등록하기

    https://developers.kakao.com/apps/
    
    여기서 앱 만들고 설정 > 일반 > 플랫폼 > 웹 > 사이트 도메인 에서 도메인 등록


- 카카오페이와 제휴하기

    - 실서비스에서는 카카오페이 파트너 제휴를 맺어야 함.
    - 카카오페이 api는 mockup용 api로 테스트 가능
    - (파트너 어드민 관련 문의나 제휴 신청은 kakaopay_partner@kakaocorp.com 으로)


- 사용되는 ID

    - **GID**   가맹점 그룹 코드. 하위에 CID들이 있음. 10자리 ()
    - **CID**   가맹점 코드. 결제 단위를 정의. 10자리 (TC0ONETIME << 테스트용. 실서버에서 사용하려면 메일 보내야 함. 발급 2주 정도 걸림)
    - **TID**	결제 한 건에 대한 고유번호. 20자리 
    - **SID**	정기결제에 사용되는 고유번호. 20자리
    - **AID**	결제, 취소, 정기결제 API 호출에 대한 고유번호. 20자리


- 결제에 필요한 필수 값

    - partner_order_id : 결제건에 대한 가맹점의 주문번호
    - partner_user_id: 가맹점에서 사용자를 구분할 수 있는 id
    - pg_token : 사용자의 결제수단 선택 완료 후 결제 대기화면에서 approval_url로 redirect할 때 request param으로 붙여서 전달해줌


- 결제 프로세스

    1. 서버에서 결제준비 API를 호출합니다.
    2. 사용자정보 입력 화면에서 사용자는 전화번호와 생년월일을 입력합니다.
    3. 결제대기 화면은 approval_url로 redirect됩니다.
    4. 결제승인 API를 호출합니다.


- 단건결제프로세스

    CID : TC0ONETIME (테스트용임)

        POST /v1/payment/ready HTTP/1.1
        Host: kapi.kakao.com
        Authorization: KakaoAK 6cf3e305cb5a28bc5f2459a3f0e9a1e1
        Content-type: application/x-www-form-urlencoded;charset=utf-8
        
        curl -v -X POST 'https://kapi.kakao.com/v1/payment/ready' \
        -H 'Authorization: KakaoAK 6cf3e305cb5a28bc5f2459a3f0e9a1e1' \
        --data-urlencode 'cid=TC0ONETIME' \
        --data-urlencode 'partner_order_id=asdfsfsfnowf123123sdlf' \
        --data-urlencode 'partner_user_id=user124642' \
        --data-urlencode 'item_name=초코파이' \
        --data-urlencode 'quantity=1' \
        --data-urlencode 'total_amount=2200' \
        --data-urlencode 'vat_amount=200' \
        --data-urlencode 'tax_free_amount=0' \
        --data-urlencode 'approval_url=https://developers.kakao.com/success' \
        --data-urlencode 'fail_url=https://developers.kakao.com/fail' \
        --data-urlencode 'cancel_url=https://developers.kakao.com/cancel'

참고로 url은 내 카카오 계정 어플리케이션에서 등록된 도메인만 됨

response는 다음과 같다.

    {"tid":"T25010464041972222222",
    "tms_result":false,
    "next_redirect_app_url":"https://mockup-pg-web.kakao.com/v1/e989df74280e07c8716e6aa4782adf775c311da1ee6bb4fba545e1db3c17bb36/aInfo",
    "next_redirect_mobile_url":"https://mockup-pg-web.kakao.com/v1/e989df74280e07c8716e6aa4782adf775c311da1ee6bb4fba545e1db3c17bb36/mInfo",
    "next_redirect_pc_url":"https://mockup-pg-web.kakao.com/v1/e989df74280e07c8716e6aa4782adf775c311da1ee6bb4fba545e1db3c17bb36/info",
    "android_app_scheme":"kakaotalk://kakaopay/pg?url=https://mockup-pg-web.kakao.com/v1/e989df74280e07c8716e6aa4782adf775c311da1ee6bb4fba545e1db3c17bb36/order",
    "ios_app_scheme":"kakaotalk://kakaopay/pg?url=https://mockup-pg-web.kakao.com/v1/e989df74280e07c8716e6aa4782adf775c311da1ee6bb4fba545e1db3c17bb36/order",
    "created_at":"2018-06-14T19:37:24"}