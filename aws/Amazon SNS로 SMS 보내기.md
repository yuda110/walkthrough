## AWS SMS

#### 기본 개념
- 주제: 주제는 메시지 전송 및 알림 구독을 위한 커뮤니케이션 채널
- 구독: 구독 대상자는 HTTP/HTTPS, Email, SMS, Amazon SQS, Lambda 등이 될 수 있다. 이 구독 시스템을 통해 한 주제를 전체 구독자에게 배포할 수 있다. (전화번호 하나 = 구독자 하나)
- key-value 형식으로 메시지 커스터마이징이 가능함

#### 주의
- 리전을 SMS 메시징 지원하는 리전으로 변경(도쿄)

#### 설정
SNS에서 문자 메시지(SMS) 카테고리 선택 후 문자 메시지 기본 설정 업데이트
- 유형에 따라 요금 다름(프로모션-안 중요한 메시지 / 트랜잭션-중요한 메시지)
- 지출한도는 기본 월 1달러
- 로그 추적을 위해 IAM 역할 생성
- Default sender ID 입력(ex. Punda). 근데 한국은 ID 지원 안 돼서 필요없음.
- 일일사용보고서 저장하려면 S3 버킷 지정

#### Python 예시
다음 코드 실행하면 저 TopicArn 구독자들에게 메시지가 전송됨(현재 2명 구독 메시지 확인)
[publish() 속성 확인](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.publish)

    import boto3

    client = boto3.client(
        "sns",
        aws_access_key_id="",
        aws_secret_access_key="",
        region_name="ap-northeast-1" # 도쿄
    )

    # 구독자 추가
    topic_arn = 'arn:aws:sns:ap-northeast-1:xxxxxxxx:My-Alert'
    client.subscribe(
        TopicArn=topic_arn,
        Protocol='sms',
        Endpoint='+8201012345678'
    )

    client.publish(
        TopicArn=topic_arn ,
        Message="파이썬 코드로 문자 보내기"
    )