#!/bin/bash

ldconfig 2>/dev/null || echo 'unable to refresh ld cache, not a big deal in most cases'

# Run initial_check.py and check if it succeeds
if ! python3 /initial_check.py; then
    echo "Initial check failed. Exiting now."
    exit 1
fi

# Proceed only if the check passed
exec text-generation-launcher $@