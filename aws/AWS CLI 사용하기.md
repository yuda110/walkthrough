# AWS CLI 사용하기

### 설치
1. 설치 관리자 다운로드
    ```
    curl "https://d1vvhvl2y92vvt.cloudfront.net/awscli-exe-macos.zip" -o "awscliv2.zip"
    ```
2. 설치 관리자 압축 풀기
    ```
    unzip awscliv2.zip
    ```
3. 설치 프로그램 실행
    ```
    sudo ./aws/install
    ```
4. 설치 확인
    ```
    aws2 --version
    ```
[자습서 링크](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/install-cliv2-macOS.html)


### 구성 및 자격증명 파일 설정
- 파일이 있는 장소
  ```
  ls  ~/.aws
  ```
> 중요한 자격 증명 정보는 `~/.aws/credentials`에, 
덜 중요한 구성 옵션은 `~/.aws/config`에 저장

    - 
    ```
    [default]
    aws_access_key_id=AKIAIOSFODNN7EXAMPLE
    aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
    ```
