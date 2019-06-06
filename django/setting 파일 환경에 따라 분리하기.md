setting 파일 환경에 따라 분리하기
--

1. `my_project/my_project` 아래에 settings 폴더를 만든 뒤,
기존 세팅파일을 `base.py`로 저장한다.

2. `dev.py`, `prod.py`, `local.py` 등 환경에 따른 세팅파일을 추가한다.

3. 이 파일들에서 `base.py`를 import 한다. 
```python
from .base import *
...
```

runserver 명령을 할 때 
`--setting=my_project.settings.dev` 이렇게 옵션을 붙여준다.
