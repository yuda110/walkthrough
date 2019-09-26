# SECRET_KEY 관리

#### mac local
```
vi ~/.zshrc || .bashrc || .bash_profile || etc
```
add this at the end of the file
```
export SECRET_KEY="xxxxxxxxxx"
```
and reboot

#### AWS Elastic Beanstalk
    
> Configuration > Software > Environment properties
