# Create a container group in US
# The access domain name will be generated to access the application

from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import CreateContainerGroup
import os
from dotenv import load_dotenv
load_dotenv()

SALAD_API_KEY = os.getenv("SALAD_API_KEY","")
ORGANIZATION_NAME = os.getenv("ORGANIZATION_NAME","")
PROJECT_NAME = os.getenv("PROJECT_NAME","")

########################################
########################################

TF_TOKEN = os.getenv("TF_TOKEN","")
API_KEY = os.getenv("API_KEY","")

VERSION = "-3090-003"
IMAGE = "saladtechnologies/llmbenchmark:003-dsr1-l8"

########################################
########################################

GROUP_NAME = "aaa-deekseek-r1-llama-8b-tgi3"+VERSION

sdk = SaladCloudSdk(
    api_key=SALAD_API_KEY, 
    timeout=10000
)

request_body = CreateContainerGroup(
   name=GROUP_NAME,        
   display_name=GROUP_NAME,
   container={
       "image": IMAGE,
       "resources": {
           "cpu": 8,
           "memory": 24576,
           "gpu_classes": ['a5db5c50-cbcb-4596-ae80-6a0c8090d80f'],
           "storage_amount": 26843545600,
       },  # 25 GB
       "priority": "high",
       "environment_variables": {'HF_TOKEN': TF_TOKEN, 
                                 'HF_HUB_ENABLE_HF_TRANSFER': '0', 
                                 'MODEL_ID': 'deepseek-ai/DeepSeek-R1-Distill-Llama-8B', 
                                 'HOSTNAME': '::', 
                                 'PORT': '80', 
                              #  'MAX_TOTAL_TOKENS': '4096', 
                              #  'MAX_INPUT_LENGTH': '2048', 
                              #  'MAX_CONCURRENT_REQUESTS': '4', 
                              #  'MAX_BATCH_SIZE': '4', 
                                 'API_KEY': API_KEY},
   },
   autostart_policy=False,
   restart_policy="always",
   replicas=5,
   country_codes=[ "us" ], 
   networking={
       "protocol": "http",
       "port": 80,
       "auth": False,
       "load_balancer": "least_number_of_connections",
       "single_connection_limit": False,
       "client_request_timeout": 100000,
       "server_response_timeout": 100000
   },
   startup_probe={
        "http": {
            "path": "/health",
            "port": 80,
            "scheme": "http",
            "headers": []
        },   
        "initial_delay_seconds": 300,
        "period_seconds": 5,
        "timeout_seconds": 3,
        "success_threshold": 1,
        "failure_threshold": 300,
   },
   readiness_probe={
        "http": {
            "path": "/health",
            "port": 80,
            "scheme": "http",
            "headers": []
        },   
        "initial_delay_seconds": 0,
        "period_seconds": 5,
        "timeout_seconds": 3,
        "success_threshold": 1,
        "failure_threshold": 3,
   },
)

print(request_body)


result = sdk.container_groups.create_container_group(
   request_body=request_body,
   organization_name=ORGANIZATION_NAME,
   project_name=PROJECT_NAME
)
print(result)

result = sdk.container_groups.get_container_group(
    organization_name=ORGANIZATION_NAME,
    project_name=PROJECT_NAME,
    container_group_name=GROUP_NAME 
)
print(result)
