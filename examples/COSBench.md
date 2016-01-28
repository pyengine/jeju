# About COSBench

Keyword | Value
----    | ----
GIT     | https://github.com/intel-cloud/cosbench.git
VERSION | origin/0.4.1.0

# Installation

## Installing Curl

~~~bash
apt-get update
apt-get -y install curl
apt-get -y install git
apt-get -y install openjdk-7-jre
~~~

# Installing COSBench

## Preparation

~~~bash
git clone ${GIT}
cd cosbench
git checkout ${VERSION} -b test
./pack.sh ${VERSION}
~~~


