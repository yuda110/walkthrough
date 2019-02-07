# Django distinct()

[django 문서](https://bit.ly/2WtmpbC) 참고

`distinct()`는 쿼리 결과에서 중복되는 데이터를 제거한다.
SQL 쿼리에서 **SELECT DISTINCT** 역할을 한다고 보면 된다.

기본적으로 쿼리셋은 중복되는 열을 제거해주지 않지만, 
흔히 사용하는 심플한 쿼리문(예를 들어 **Blog.objects.all()**)에서는 결과가 중복될 일이 거의 없다.
하지만 데이터베이스가 점점 커지고 테이블이 많아진다면 중복된 결과를 가져올 확률이 높아진다.

그럴 때 `distinct()`가 필요하다.

---

다만, `distinct()`를 

`distinct()`는 `order_by()`와 함께 사용해야 한다.


 [스택오버플로](https://bit.ly/2Usq1IN) 참고