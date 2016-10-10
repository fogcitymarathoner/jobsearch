#!/bin/bash
# myapp daemon
# chkconfig: 345 20 80
# description: myapp daemon
# processname: myapp
PROJECT_DIR="/home/marc/python_apps/jobsearch/"
APP_DIR="/home/marc/python_apps/jobsearch/"
DAEMON_PATH=$PROJECT_DIR"bin/"

DAEMON=/home/marc/envs/jobs/bin/uwsgi
INI_HOME=/etc/uwsgi/apps-enabled/
INI_FILE='jobsearch.com.8088.ini'
DAEMONOPTS=" "${INI_HOME}${INI_FILE}

NAME=fogtest
DESC="fogtest daemon description"
PIDFILE=$APP_DIR"pid.txt"
SCRIPTNAME=/etc/init.d/$NAME

case "$1" in
start)
	printf "%-50s" "Starting $NAME..."
	cd $APP_DIR
	PID=`$DAEMON $DAEMONOPTS > /dev/null 2>&1 & echo $!`
	#echo "Saving PID" $PID " to " $PIDFILE
        if [ -z $PID ]; then
            printf "%s\n" "Fail"
        else
            echo $PID > $PIDFILE
            printf "%s\n" "Ok"
        fi
;;
status)
        printf "%-50s" "Checking $NAME..."
        if [ -f $PIDFILE ]; then
            PID=`cat $PIDFILE`
            if [ -z "`ps axf | grep ${PID} | grep -v grep`" ]; then
                printf "%s\n" "Process dead but pidfile exists"
            else
                echo "Running"
            fi
        else
            printf "%s\n" "Service not running"
        fi
;;
stop)
        printf "%-50s" "Stopping $NAME"
            PID=`cat $PIDFILE`
            cd $PROJECT_DIR
        if [ -f $PIDFILE ]; then
            kill -9 $PID
            printf "%s\n" "Ok"
            rm -f $PIDFILE
        else
            printf "%s\n" "pidfile not found"
        fi
;;

restart)
  	$0 stop
  	$0 start
;;

*)
        echo "Usage: $0 {status|start|stop|restart}"
        exit 1
esac
