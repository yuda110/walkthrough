Abstract Syntax Trees
===
**Abstract Syntax Trees**, ASTs, are a powerful feature of Python.

Getting to and from ASTs
---
ast를 하려면,
- store code as a string
- use `ast.parse()`
- To turn the ast into executable code, pass it to `compile()`

```
>>> tree = ast.parse("print('hello world')")
>>> tree
<_ast.Module object at 0x9e3df6c>
>>> exec(compile(tree, filename="<ast>", mode="exec"))
hello world
```

####Modes
Python 코드는 세 가지 모드로 컴파일될 수 있다.
- exec
    - 보통 Python 코드는 `mode='exec'`을 사용한다.
- eval
    - eval은 single expression만을 받는다.
    - 쉽게 말해서, 
    ```
    >>> exec('a = 47')
    >>> a
    >>> 47
    ```
    은 가능하지만,
    ```
    >>> eval('a = 47')
    Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1
    a = 47
      ^
    SyntaxError: invalid syntax
    ```
    은 안 됨.

  - 함께 읽으면 좋은 글: 
  [Eval really is dangerous](https://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html)

