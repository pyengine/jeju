# Execute Python code

To do execute python code, use 'python' as language

~~~python

def do_something():
    print "This is python code"

do_something()
~~~

# Replace by environment variable

To use environment variable, make table with Keyword, Value, Description(optional).
Before executing code, ${VARIABLE} is replace by environment value

Keyword | Value | Description
---- | ---- | ----
MY_ID | "choonho" | This is environment value


~~~python

def do_something(name):
    print "My name is %s" % name

do_something(${MY_ID})
~~~
