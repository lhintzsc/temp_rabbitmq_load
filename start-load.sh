#!/bin/bash

echo "fill queue"
./while_send.sh &
./while_receive.sh &

echo "fill exchange"
./while_emit_log.sh &
./while_receive_log.sh &
