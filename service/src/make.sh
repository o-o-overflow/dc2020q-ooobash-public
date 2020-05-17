#!/bin/bash

set -x

# clean your own source tree
cd ./ooobash-src/bash-5.0/
make clean
rm -f ./Makefile ./builtins/Makefile
cd -

docker kill "making-ooobash"
docker rm "making-ooobash"

docker build -t make-ooobash .


docker run --name "making-ooobash" -i --rm -d make-ooobash

docker exec "making-ooobash" mkdir /makebash

docker cp "./ooobash-src/bash-5.0" "making-ooobash":/makebash/bash-5.0

# docker exec "making-ooobash" bash -c "cd /makebash/bash-5.0/ && ./configure CFLAGS='-s -O2 -no-pie' LDFLAGS='-s -O2 -no-pie' && make clean && make"
docker exec "making-ooobash" bash -c "cd /makebash/bash-5.0/ && ./configure && make clean && make -j4"

docker cp "making-ooobash":/makebash/bash-5.0/bash ../ooobash

docker kill "making-ooobash"
