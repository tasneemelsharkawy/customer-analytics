#!/bin/bash

mkdir -p customer-analytics/results/

docker cp customer-analytics-run:/app/pipeline/data_raw.csv customer-analytics/results/
docker cp customer-analytics-run:/app/pipeline/data_preprocessed.csv customer-analytics/results/
docker cp customer-analytics-run:/app/pipeline/insight1.txt customer-analytics/results/
docker cp customer-analytics-run:/app/pipeline/insight2.txt customer-analytics/results/
docker cp customer-analytics-run:/app/pipeline/insight3.txt customer-analytics/results/
docker cp customer-analytics-run:/app/pipeline/summary_plot.png customer-analytics/results/
docker cp customer-analytics-run:/app/pipeline/clusters.txt customer-analytics/results/

docker stop customer-analytics-run
docker rm customer-analytics-run
