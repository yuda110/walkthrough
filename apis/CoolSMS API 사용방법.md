# CoolSMS API 사용 방법

참고: https://www.coolsms.co.kr/Python_SDK_Start_here

국내 SMS API 서비스를 제공하는 업체 중 하나로, REST API 및 Python SDK로 구현가능하다.

### Step 1. Python SDK를 설치한다.
    
    
    $ pip install coolsms_python_sdk
    

### Step 2. CoolSMS에 회원가입한다.

### Step 3. API 키를 발급받는다.
![Alt CoolSMS 1](/images/coolsms1.png)

### Step 4. Python에서 발신번호를 등록한다.
테스트를 하기 위해서는 발신번호를 등록해야 한다. 
발신번호 등록에는 1) Python으로 등록 2) 웹에서 등록 두 가지 방법이 있다.

#### [파이썬으로 등록하는 방법](https://www.coolsms.co.kr/Python_SDK_EXAMPLE_SenderID)
	import sys
	from sdk.api.sender_id import SenderID 
	from sdk.exceptions import CoolsmsException

	##  @brief This sample code demonstrate how to request sender number register through CoolSMS Rest API
	if __name__ == "__main__":
	    # set api key, api secret
	    api_key = "#ENTER_YOUR_OWN#"
	    api_secret = "#ENTER_YOUR_OWN#"

	    # phone is mandatory.
	    phone = "01000000000"

	    cool = SenderID(api_key, api_secret)

	    try:
	        response = cool.register(phone)
	        print("ARS Number : %s" % response['ars_number'])
	        print("Handle Key : %s" % response['handle_key'])

	    except CoolsmsException as e:
	        print("Error Code : %s" % e.code)
            print("Error Message : %s" % e.msg)

        sys.exit()

#### 웹으로 등록하는 방법
웹으로 발신번호를 등록하려면 전화인증 혹은 서류인증이 필요하며 전화인증은 6개월, 서류인증은 1년마다 갱신해야 한다. 
참고로 전화인증이 훨씬 간단하다.

### Step 5. Python에서 단문 메시지 보내기

	import sys
	from sdk.api.message import Message
	from sdk.exceptions import CoolsmsException

	##  @brief This sample code demonstrate how to send sms through CoolSMS Rest API PHP
	if __name__ == "__main__":

        # set api key, api secret
        api_key = "#ENTER_YOUR_OWN#"
        api_secret = "#ENTER_YOUR_OWN#"

        ## 4 params(to, from, type, text) are mandatory. must be filled
        params = dict()
        params['type'] = 'sms' # Message type ( sms, lms, mms, ata )
        params['to'] = '01000000000' # Recipients Number '01000000000,01000000001'
        params['from'] = '01000000000' # Sender number
        params['text'] = 'Test Message' # Message

        cool = Message(api_key, api_secret)
        try:
            response = cool.send(params)
            print("Success Count : %s" % response['success_count'])
            print("Error Count : %s" % response['error_count'])
            print("Group ID : %s" % response['group_id'])

            if "error_list" in response:
                print("Error List : %s" % response['error_list'])

        except CoolsmsException as e:
            print("Error Code : %s" % e.code)
            print("Error Message : %s" % e.msg)

        sys.exit()



