# Devstack Installation Guide

# Environment

Prerequisite

Keyword | Value
---- | ----
USER | root

# Add stack user
~~~bash
adduser stack

echo "stack ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
~~~


# Download source code

Keyword | Value
---- | ----
USER | stack
PWD  | /home/stack

~~~bash
git clone https://github.com/openstack-dev/devstack.git
~~~

# edit localrc

[<img src="https://raw.githubusercontent.com/analytaps/jeju/master/examples/devstack_single.jpg">](http://docs.openstack.org/developer/devstack/)

edit devstack/localrc

~~~text
# default
 
# network
FLAT_INTERFACE=eth1
FIXED_RANGE=10.0.0.0/20
FIXED_NETWORK_SIZE=4096
FLOATING_RANGE=192.168.0.1/24
 
# vnc
VNCSERVER_LISTEN=0.0.0.0
 
# logs
DEST=/opt/stack
LOGFILE=$DEST/logs/stack.sh.log
SCREEN_LOGDIR=$DEST/logs/screen
 
# system password
ADMIN_PASSWORD=openstack
MYSQL_PASSWORD=openstack
RABBIT_PASSWORD=openstack
SERVICE_PASSWORD=openstack
SERVICE_TOKEN=openstackservicetoken
 
# cinder
VOLUME_GROUP="cinder-volume"
VOLUME_NAME_PREFIX="volume-"
~~~

# run stack.sh

stack.sh is bootstrap script.

~~~bash
cd devstack
git branch -r
echo "You can use branch..."
git checkout stable/kilo
./stack.sh
~~~

