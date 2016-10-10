#!/bin/bash
#
# Runs the WSGI server.
#
uwsgi --uwsgi localhost:8088  --logto log.txt --pidfile=pid.txt --touch-reload=reload --wsgi-file /home/marc/python_apps/jobsearch/wsgi.py
#while [ true ] ; do
#done

