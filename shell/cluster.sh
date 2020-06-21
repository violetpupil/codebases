#!/usr/bin/env bash
# 发送命令到集群中的每个节点

# -z 判断变量是否为空
# $1 执行该脚本时的第一个参数
if [ -z $1 ]
then
	echo "请指定需要执行的命令!"
	exit
fi

# 指定节点
for i in 1 2 3
do
	echo node-$i
	# 发送命令并执行
	ssh node-$i "source /etc/profile; $1"
	echo
done