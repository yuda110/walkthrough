# header 주의사항

서비스 API를 사용할 때 레퍼런스를 잘 보고 
**request**에 별도로 명시된 header가 있다면 지켜야 한다.

ex.
pipedrive API를 사용할 때, `PUT`메소드의 경우 명시된 header를 사용하지 않았더니 
status가 200임에도 전혀 작동하지 않았다.
