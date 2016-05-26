###########################################
# This is very naive replacement algorithm
# TODO
############################################
import subprocess
import string
import uuid
import logging
import sys

# TODO: configurable variable
TEMP_DIR = "/tmp"

def replaceable(code, kv):
    # change keyword to value
    keys = kv.keys()
    # find keyword which is ${keyword}
    # replace value ${keyword} <- kv[keyword]
    for key in keys:
        nkey = "${%s}" % key
        code = string.replace(code, nkey, kv[key])
    logging.debug("#" * 20 + "\n%s" % code)
    logging.debug("#" * 20)

    return code

def execute_python(**kwargs):
    code = kwargs['code']
    kv = kwargs['kv']

    import os
    # call replaceable
    rcode = replaceable(code, kv)

    temp = uuid.uuid1()
    temp_file = "%s/%s" % (TEMP_DIR, str(temp))

    fp = open(temp_file, 'w')
    fp.write(rcode)
    fp.close()

    # Execute Cmd
    
    cmd = ['python',temp_file]
    cmd2 = 'python %s' % temp_file
    #subprocess.call(cmd)
    proc = subprocess.Popen(cmd)
    (out, err) = proc.communicate()
    #out = subprocess.check_output(cmd, stdout=subprocess.STDOUT)
    os.remove(temp_file)
    return {'input':rcode, 'output':out, 'error':''}

