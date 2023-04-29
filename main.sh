#!/bin/bash

PORTS=(7001 7002 7003 7004 7005 7006)

rm -f appendonly.aof
rm -f dump.rdb

for port in "${PORTS[@]}"; do
    rm -rf "$port"
    mkdir "$port"
    touch "$port/redis.conf" "$port/nodes.conf"
    cat << EOF > "$port/redis.conf"
port $port
cluster-enabled yes
cluster-config-file $port/nodes.conf
cluster-node-timeout 5000
appendonly yes
EOF
done

redis_pids=()
for port in "${PORTS[@]}"; do
    redis-server "./$port/redis.conf" &
    redis_pids+=($!)
done

sleep 5

redis-cli --cluster create $(printf '127.0.0.1:%s ' "${PORTS[@]}") --cluster-replicas 1

for pid in "${redis_pids[@]}"; do
    wait "$pid"
done