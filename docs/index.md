# Introduction

Jeju is intelligent provisioning system based on specification documents
Each S/W project has instruction documents like REAME.md, INSTALL.md ...

User can manually insall program based on INSTALL.md
But the document may be ambiguously described.
Jeju can automatically install the software instructed by INSTALL.md

## Architecture

<img src="https://raw.githubusercontent.com/pyengine/jeju/master/docs/jeju_architecture.png">

Other methods like cher, puppet, ansible ...

<img src="https://raw.githubusercontent.com/pyengine/jeju/master/docs/other_method.png">

This can help developer and user.
# History

Version | Description
----    | ----
0.3     | Support Yaml configuration update
0.3.2   | Support fine grained logging /var/log/jeju.log
0.3.4   | Fix ini editor bug
0.3.5   | Better console output

# Installation
Jeju is python program. This can be easily installed by pip.
If pip is not exist, run *apt-get install python-pip* or *yum install python-pip*

Jeju supports various syntax, the dependency packages are:

Syntax  | Package
----    | ----
yaml    | ruamel.yaml, gcc
expect  | expect

## RedHat, CentOS

~~~bash
yum install python-devel gcc expect python-pip
pip install jeju
~~~

## Debian, Ubuntu

~~~bash
apt-get update
apt-get install python-dev gcc expect python-pip
pip install jeju
~~~

# How to run

If you want to know detailed options.

~~~bash
jeju -h
~~~

Usage:

~~~bash
jeju -m <markdown guide book>
~~~

# Guide Book

You can see many examples in jeju guide-book repository.


[https://github.com/pyengine/jeju-guide](https://github.com/pyengine/jeju-guide)

