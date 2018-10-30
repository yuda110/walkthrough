# 아임포트 API 사용 방법

http://www.iamport.kr

- 엄청 쉬움
- 웹 이니시스로 하면 카카오페이 비롯 모든 카드 다 됨

- 적용 예시

        function PayWithIamport(pg) {
          let IMP = window.IMP; // 생략해도 됨
          IMP.init("imp38584119"); // 가맹점 식별코드
        
          IMP.request_pay({
            pg : pg,//'html5_inicis',
            pay_method : 'card',
            merchant_uid : 'merchant_' + new Date().getTime(),
            name : '테스트',
            amount : 1000,
            buyer_email : 'aydha0110@gmail.com',
            buyer_name : '내이름',
            buyer_tel : '010-1234-5678',
            buyer_addr : '서울특별시 땡땡로',
            buyer_postcode : '01234'
          }, function(rsp) {
            if (rsp.success) {
              let msg = '결제가 완료되었습니다.';
              msg += '고유ID : ' + rsp.imp_uid;
              msg += '상점 거래ID : ' + rsp.merchant_uid;
              msg += '결제 금액 : ' + rsp.paid_amount;
              msg += '카드 승인번호 : ' + rsp.apply_num;
              alert(msg);
              location.reload();
            } else {
              let msg = '결제에 실패하였습니다.';
              msg += '에러내용 : ' + rsp.error_msg;
              alert(msg);
              location.reload();
            }
          });
        }