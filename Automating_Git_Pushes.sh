#!/bin/bash

# Variables
COMMIT_MSG=$1

# Add all files
git add .

# Commit with a message
git commit -m "$COMMIT_MSG"

# Push to repository
git push origin main

echo "Changes pushed to the repository."

# uj sor