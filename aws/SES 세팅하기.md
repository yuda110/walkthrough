# AWS SES


- postfix는 host나 domain 등 직접 설정하는 게 많다.
- 따로 인증절차를 거치지 않은 경우 메일이 암호화되지 않아 스팸 메일로 들어가게 된다.
- AWS SES를 사용하면 신경 쓸 요소들이 대폭 줄어든다.
- 가격도 저렴하다. 1,000건 이하는 무료이며 초과할 시 1,000건 당 10센트를 지불한다.


### 다른 AWS 서비스들과 함께
- **EC2** 인스턴스에 이메일 기능을 추가할 수 있다.
- **Amazon Simple Notification Service (Amazon SNS)**: 메일이 성공적으로 전송되었거나 반송되거나 뭔가 오류가 있을 때 알람을 수신할 수 있다.
- **AWS Identity and Access Management(IAM)**: 이메일 전송에 대한 사용자 엑세스를 제어할 수 있다.
- **Route 53**: 함께 사용하면 더 편리하다.
- **Amazon Simple Storage Service(Amazon S3)**: 수신 이메일 저장 가능
- **AWS Lambda**: 함수를 트리거해서 수신 이메일에 여러 가지 작업 가능
- **AWS Key Management Service(AWS KMS)**: S3 버킷에 수신하는 메일을 암호화
- **AWS CloudTrail**: 콘솔 또는 Amazon SES API를 사용해 Amazon SES API 호출 내역을 기록


## 이메일 설정
### 자격 증명 확인 > 이메일 주소 확인
1) `Identity Management`에서 `Email Addresses` 버튼을 누른다.
2) `Verify a New Email Address` 버튼을 누른다.
3) 등록한 이메일로 온 인증 메일의 링크를 누르면 `Verification Status`가 `verified`로 변경된다.
![Alt SES 1](/images/ses1_1.png)
4) 아래의 파일을 적당히 수정하여 `customverificationemail.json`으로 저장한 뒤, 


    {
      "TemplateName": "SampleTemplate",
      "FromEmailAddress": "sender@example.com",
      "TemplateSubject": "Please confirm your email address",
      "TemplateContent": "<html>
                          <head></head>
                          <body style="font-family:sans-serif;">
                            <h1 style="text-align:center">Ready to start sending 
                            email with ProductName?</h1>
                            <p>We here at Example Corp are happy to have you on
                              board! There's just one last step to complete before
                              you can start sending email. Just click the following
                              link to verify your email address. Once we confirm that 
                              you're really you, we'll give you some additional 
                              information to help you get started with ProductName.</p>
                          </body>
                          </html>",
      "SuccessRedirectionURL": "https://www.example.com/verifysuccess",
      "FailureRedirectionURL": "https://www.example.com/verifyfailure"
    }

다음 명령어로 템플릿을 생성한다.(**file://** 반드시 들어가야 함)

    > aws ses create-custom-verification-email-template --cli-input-json file://customverificationemail.json
    
템플릿이 생성됐는지 확인하려면 다음 명령어를 친다.

    > aws ses list-custom-verification-email-templates
    
이 템플릿은 UpdateCustomVerificationEmailTemplate API 로 수정할 수 있다.

### 자격 증명 확인 > 도메인 확인
1) SES에서 **Verify a New Domain** 버튼을 눌러 도메인을 넣어준다.
![Alt SES 1](/images/ses2_1.png)

2) **Domain Verification Record Set**을 확인한 뒤 나의 도메인 DNS 설정에 추가해준다.
외부 도메인 서비스가 아닌 AWS Route 53을 사용할 경우, 
동일 계정으로 AWS Management 콘솔에 로그인하면 SES 콘솔 내에서 즉시 DNS 서버를 업데이트한다. 
![Alt SES 2](/images/ses2_2.png)

3) 완료하고 나면 이렇게 추가된 도메인이 보일텐데, AWS가 DNS 설정을 확인하기까지는 최대 48시간이 걸리나 보통 이보다 훨씬 빨리 적용된다. 
확인되고 나면 `Verification Status`가 **pending verification**에서 **verified**로 변경된다. 실패하면 **failed**가 뜬다.
![Alt SES 3](/images/ses2_3.png)

