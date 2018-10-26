# celery flower

- flower는 celery를 웹에서 모니터링할 수 있게 해주는 툴이다.

    
    
### flower 설치
    $ pip install flower
    
### init.d에 flower.sh 혹은 flower 생성

    $ sudo touch /etc/init.d/[file-name].sh
    $ sudo chmod 755 /etc/init.d/[file-name]
    $ sudo chown root:root /etc/init.d/[file-name]

### init 파일 내용 작성

        #!/bin/bash
        ### BEGIN INIT INFO
        # Provides:             flower
        # Required-Start:       $network $local_fs $remote_fs
        # Required-Stop:        $network $local_fs $remote_fs
        # Default-Start:        2 3 4 5
        # Default-Stop:         0 1 6
        # Short-Description:    celery flower daemon
        ### END INIT INFO
        
        NAME=flower
        DESC="flower daemon"
        
        # Name of the projects settings module.
        export DJANGO_SETTINGS_MODULE="yourproject.settings"
        
        # Path to virtualenv
        ENV_PYTHON="/your/virtualenv/bin/python"
        
        # Where the Django project is.
        FLOWER_CHDIR="/path/to/your/project"
        
        # How to call "manage.py celery flower" (args...)
        FLOWERCTL="/your/virtualenv/bin/flower -port=5555"
        DAEMON=$FLOWERCTL
        
        set -e
        
        case "$1" in
          start)
                echo -n "Starting $DESC: "
        
                # Activate the virtual environment
                . /your/virtualenv/bin/activate
        
                start-stop-daemon --start --pidfile /var/run/$NAME.pid \
                    --chdir $FLOWER_CHDIR --chuid celery \
                    --user celery --group celery --background \
                    --make-pidfile \
                    --exec "$ENV_PYTHON" -- $FLOWERCTL
                echo "$NAME."
                ;;
        
          stop)
                echo -n "Stopping $DESC: "
                start-stop-daemon --stop --quiet --oknodo \
                    --pidfile /var/run/$NAME.pid
                rm -f /var/run/$NAME.pid
                echo "$NAME."
                ;;
        esac
        
        exit 0




###참고

- https://flower.readthedocs.io/en/latest/
- https://github.com/mher/flower/issues/717
- https://gist.github.com/rodrigogadea/8230898 
