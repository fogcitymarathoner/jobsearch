#!/home/rocketsr/bin/python
import sys, os
##############################################################
# Add a custom Python paths
#
project_sys="/home/rocketsr/django"
sys.path.insert(0, project_sys)
#
project_sys="/home/rocketsr/django_vendor_libs/webpymail"
sys.path.insert(0, project_sys)
#
project_sys="/home/rocketsr/django_libs"
sys.path.insert(0, project_sys)
#
project_sys="/home/rocketsr/django_vendor_libs"
sys.path.insert(0, project_sys)
###############################################################

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "cms.settings" 

from django.core.servers.fastcgi import runfastcgi
#runfastcgi(method="threaded")
runfastcgi(["method=threaded", "daemonize=false"])
