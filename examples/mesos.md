# System Requirements

# Environment

Keyword   | Value
----  | ----
VERSION | 0.25.0
IP      | 127.0.0.1
WORK_DIR | /data/mesos


~~~bash
apt-get update
apt-get install -y openjdk-7-jdk
apt-get install -y autoconf libtool
apt-get install -y build-essential python-dev python-boto libcurl4-nss-dev libsasl2-dev maven libapr1-dev libsvn-dev zlib1g-dev
~~~

# Building Mesos

~~~bash
wget http://www.apache.org/dist/mesos/${VERSION}/mesos-${VERSION}.tar.gz
tar -zxf mesos-${VERSION}.tar.gz

cd mesos-${VERSION}

mkdir build
cd build
../configure
make -j 8
make check
make install
~~~

# Run Mesos master

~~~bash
./build/bin/mesos-master.sh --ip=${IP} --work_dir=${WORK_DIR} &
~~~
