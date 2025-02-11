from imds_reallocate import Reallocate
from check_gpu import Get_CUDA_Version,Get_GPU
import sys
import uuid
import os

# If run the container locally, use a random ID
LOCAL_MACHINE = str(uuid.uuid4()) 
# Get the ID if running on SaladCloud
salad_machine_id = os.getenv("SALAD_MACHINE_ID", LOCAL_MACHINE)

# True if running locally  
g_local_run = True if salad_machine_id == LOCAL_MACHINE else False

g_CUDA_version = Get_CUDA_Version()
if g_CUDA_version <= 12.2:
    Reallocate(g_local_run, "low cuda version")

g_GPU = Get_GPU()
g_VRAM_free = float(g_GPU['vram_free'].split(" ")[0])
if g_VRAM_free < 23000: # MiB
    Reallocate(g_local_run, "low VRAM")

print("The initial check passed!")

sys.exit(0)



