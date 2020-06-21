#!/usr/bin/env bash
# 控制zookeeper集群
# start 启动 stop 停止 status 查看状态 restart 重启

cmd=$1
# 如果没有参数，默认启动
# -z 判断变量是否为空
if [ -z $cmd ]
then
	cmd=start
fi

echo "$cmd zookeeper cluster ..."
# 指定节点
for i in 1 2 3
do
	echo node-$i
	# 发送命令并执行
	ssh node-$i "source /etc/profile; zkServer.sh $cmd"
	echo
done