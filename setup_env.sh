#!/bin/bash
# Setup environment variables for JuankoOS deployment on GKE

export PROJECT_ID="<YOUR PROJECT ID>"
export REGION="<YOUR REGION>"
export ZONE="<YOUR ZONE>"
export CLUSTER_NAME="nim-demo"
export NODE_POOL_MACHINE_TYPE="g2-standard-16"
export CLUSTER_MACHINE_TYPE="e2-standard-4"
export GPU_TYPE="nvidia-l4"
export GPU_COUNT=1

echo "Environment variables configured."
