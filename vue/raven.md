Raven!
---

Sentry에 로깅을 보내는 client가 필요한데, Raven이 이 역할을 한다.

```javascript
npm install 'raven-js'

import Raven from "raven-js"
import RavenVue from "raven-js/plugins/vue"

Raven
    .config('https://c6686f778bef467b9ee5d33c1d1d751c@sentry.io/1223821')
    .addPlugin(RavenVue, Vue)
    .install();
```

이러면 에러가 났을 때 자동으로 Sentry에 넘겨준다. 
혹, 따로 에러 메시지를 명시하고 싶으면 다음과 같이 사용한다.

```javascript
function logException(ex, context) {
  Raven.captureException(ex, {
    extra: context
  });
}
```
