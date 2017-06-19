#!/usr/bin/env bash
# this script prints the row numbers in each table.
# note it uses map/reduce, and takes time to finish if table is large.

for t in `python get_tables.py`; do
  r=$(/usr/local/bin/hbase org.apache.hadoop.hbase.mapreduce.RowCounter $t 2>&1 | grep 'ROWS' | cut -f 2 -d '=')
  echo -e "$t\t$r"
  #echo -e "| $t\t|\t| $r\t|\t|"
done
