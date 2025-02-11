#!/bin/bash

ps -ef

echo ""
echo "Health Check - http://localhost/health"
curl http://localhost/health


