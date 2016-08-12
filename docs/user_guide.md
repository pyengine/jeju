# User Guide

Jeju can execute various programming languages.
The supported lists are:

Syntax | Suppported from
----    | ----
bash    | 0.3.5
python  | 0.3.5
text    | 0.3.5
yaml    | 0.3.5
expect  | 0.3.5

The format is write any syntax within **Code block**.

> \~\~\~syntax type
> code block
> \~\~\~

## bash

Bash is the most popular script language for automation.

You can use bash script with **bash** keyword

> \~\~\~bash
> *any bash script*
> *any bash script*
> \~\~\~

For example,

> \~\~\~bash
> echo $hostname
>\~\~\~


## Python

Python is the one of popular script language for programming.

You can use python script with **python** keyword

> \~\~\~python
> *any python language*
> *any python language*
> \~\~\~

For example,

> \~\~\~python
> import os
> os.system('hostname')
> \~\~\~

## Text

Text is used for creating new file with some content like configuration file.

Text requires file path for saving. This must be described with **edit <file path>** before **Code block** 

> edit *<file path>*
> 
> \~\~\~text
> *any text*
> *any text*
> \~\~\~


