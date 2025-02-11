#!/bin/bash

api_key=1234
model=deepseek-ai/DeepSeek-R1-Distill-Llama-8B

curl http://localhost:80/v1/chat/completions     -X POST     -d '{
  "model": "$model",
  "messages": [
    {
      "role": "system",
      "content": "You are a good guy!"
    },
    {
      "role": "user",
      "content": "How to learn AI and Machine Learning?"
    }
  ],
  "stream": true,
  "max_tokens": 512
}'     -H 'Content-Type: application/json' -H "Authorization: Bearer $api_key"
