# When QuerySets are evaluated

QuerySet은 게으르기 때문에 이 QuerySet의 결과를 가지고 무언가를 하기 전까지는 쿼리가 실행되지 않는다.
쿼리를 실행하는 트리거는 다음과 같다.

- Iteration
- Slicing
- Pickling/Caching
- repr()
- len()
- list()
- bool()


참고: [Django 문서](https://docs.djangoproject.com/ko/2.1/ref/models/querysets/#when-querysets-are-evaluated)