# certbot으로 인증서 발급받기

    $ sudo add-apt-repository ppa:certbot/certbot

    $ sudo apt-get update

    $ sudo apt-get install python-certbot-apache


-  Set up the SSL Certificate


    $ sudo certbot --apache -d [[example.com]]