#!/bin/bash
#
set -e
set -u


install_packs() {
        echo "install_packs"

        apt update

        apt full-upgrade -y

        apt-get install python -y

        apt-get install idle-python -y
        apt-get install python-pip -y
        apt-get install libmysqlclient-dev -y
        apt-get install python-dev -y
        apt-get install default-jdk -y

        apt-get install mysql-server -y
 
        apt-get install python-mysqldb -y
        apt-get install openssh-server -y
        apt-get install apache2 -y

        apt-get install phpmyadmin -y

        apt-get install git

        pip install --upgrade pip
        pip install --upgrade setuptools
        pip install MySQL-python
        pip install pymysql
        pip install django
        pip install django-secure
        pip install django-sslserver
        pip install setuptools
        pip install django-extensions

        python -V
        django-admin --version

}


#
# MAIN
#

case "${1}" in

    'install')
            install_packs
            ;;

    'fw-start')
            echo "firewall-start"
            /bin/fw.start
            ;;

    'fw-stop')
            echo "firewall-stop"
            /bin/fw.stop
            ;;

    *)
            echo ""
            echo "Usage:                                                 "
            echo "        push_to_install  install | fw.start | fw.stop  "
            echo ""
            exit 1
            ;;


esac

exit 0


