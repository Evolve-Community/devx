#!/bin/bash

docker run \
       -it --rm \
       -v `pwd`:/devx \
       -v `pwd`/tmp.benchmarks/.:/benchmarks \
       -e OPENAI_API_KEY=$OPENAI_API_KEY \
       -e HISTFILE=/devx/.bash_history \
       -e DEVX_DOCKER=1 \
       -e DEVX_BENCHMARK_DIR=/benchmarks \
       devx-benchmark \
       bash
