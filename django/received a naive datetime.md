# RuntimeWarning: DateTimeField received a naive datetime

timezone이 설정되지 않은 date가 model로 넘어갔을 때 발생하는 에러이다.

```python
from datetime import datetime

now = timezone.now()
```

이렇게 사용하는 대신 다음과 같이 사용한다.

```python
from django.utils import timezone

now = timezone.now()
```
