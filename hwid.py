from ctypes.wintypes import PSHORT
import psutil, platform, GPUtil
from hashlib import md5
uname = platform.uname()
gpus = GPUtil.getGPUs()
list_gpus = []
for gpu in gpus:
    # get the GPU id
    gpu_id = gpu.id
    # name of GPU
    gpu_name = gpu.name
HardwareInfo = ""
svmem = psutil.virtual_memory()
try:
    HardwareInfo = f"{uname.system} {uname.node} {uname.release} {uname.processor}{gpu_name}{gpu_id}"
except:
    HardwareInfo = f"{uname.system} {uname.node} {uname.release} {uname.processor}"
HWID = HardwareInfo
HWID = HWID.encode()
HWID = md5(HWID)
print(f"Hardwareinfo: {HardwareInfo}")
print(f"hwid: {HWID.hexdigest()}")

input("Press enter to close. . .")
