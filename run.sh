#!/usr/bin/env bash

# Authors: zhangzhenhu(zhangzhenhu@iwaimai.baidu.com)
# Date:    2015/12/20 16:56


__script_dir=$(cd "$(dirname "$0")"; pwd)
source ${__script_dir}/../../conf/env.sh
begin_time=`date +%s`

cd ${__script_dir}/build/html
nohup python ${__script_dir}/source/start.py >webapp.log 2>&1 &