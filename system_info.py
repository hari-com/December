###################################################
## This module is a wrapper around the platform
## module to fetch OS related information.
###################################################

__version__ = "1.0.0"

import platform, psutil, subprocess, power, GPUtil
import ctypes, os


#LOGGER = logging.getLogger(__name__)

def get_cpu_info():
    """
	Returns the CPU info from the running system
	"""
    return platform.uname().processor

def get_cpu_count():
    """
	Returns the CPU count from the running system
	"""
    return psutil.cpu_count(logical=False)

def get_cpu_usage():
    """
	Returns the CPU usage from the running system
	"""
    return psutil.cpu_percent()

def get_memory_info():
    """
	Returns the Memory info from the running system
	"""
    return psutil.virtual_memory()

def get_board_info():
    """
	Returns the Board information of the system running on
	"""
    command = "wmic bios get serialnumber"
    return os.popen(command).read().replace("\n","").replace("	","").replace(" ","")

def get_power_info():
    ans = power.PowerManagement().get_providing_power_source_type()
    if not ans:
        print ("Plugged into wall socket")
    else:
        print ("On battery")
    return None

def get_gpu_info():
    return GPUtil.getGPUs


if __name__ == "__main__":
    print ("Processor: " + get_cpu_info())
    print ("MotherBoard: " + get_board_info())
    print (get_memory_info())
    print (get_cpu_usage())
    print (get_cpu_count())
    print (get_power_info())
    print (get_gpu_info())
    