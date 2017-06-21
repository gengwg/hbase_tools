#!/usr/bin/env python
# disable and delete all hbase tables

import sys
import happybase
import datetime
import json

if happybase.__version__ < 0.9:
    sys.stderr.write("Incorrect Happybase version, expecting 0.9 found %s \n" % happybase.__version__ )
    sys.exit(1)

# hbase2 server cname
hbase2_server = 'hbase2.targeting.walmartlabs.com'

socket_timeout = 120000 # 2 minutes
# create connection pool, with 2 new parameters added in version happybase version 0.9
pool2 = happybase.ConnectionPool(size=3,
                                 host=hbase2_server,
                                 port=9090,
                                 timeout=socket_timeout,
                                 transport='framed', # new connection parameter
                                 protocol='compact'  # new connection parameter
                                )

with pool2.connection() as connection:
    try:
        tables = connection.tables()
        for t in  tables:
            connection.delete_table(t, disable=True)
    except:
        # Write to stdout
        print(sys.exc_info())



