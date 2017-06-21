#!/usr/bin/env bash

# to set hbase table to readonly
# echo "alter 'test',{METHOD=>'table_att', READONLY=>true}" | hbase shell

for table in `python get_tables.py`; do
  echo "alter '$table',{METHOD=>'table_att', READONLY=>true}" | hbase shell
done
