# Execute Yaml code

To do execute yaml code, use 'yaml' as language

edit /tmp/a.yaml

~~~text
init_config: {}
# When adding item which has sub-item, add full information,
# else you can miss some previous item. ex)host: <IP>
# This is comment, comment is reserved
instances:
    - host: <IP>              # update with IP
      username: <username>    # update with user name
      password: <password>    # update with password

~~~

# Replace by environment variable

To use environment variable, make table with Keyword, Value, Description(optional).
Before executing code, ${VARIABLE} is replace by environment value

Keyword | Value | Description
---- | ---- | ----
MY_ID | "choonho" | This is environment value
MY_PASSWORD | "123456" | This is environment value

edit /tmp/a.yaml

~~~yaml

instances:
      username: ${MY_ID} # new comment
      password: ${MY_PASSWORD}

~~~

# Check the result

~~~bash
cat /tmp/a.yaml
~~~
