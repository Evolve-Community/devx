#!/bin/bash

set -e

docker build \
       --file benchmark/Dockerfile \
       -t devx-benchmark \
       .
