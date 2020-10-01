###################################################
## This module is a wrapper around the platform
## module to fetch OS related information.
###################################################

__version__ = "1.0.0"

import platform, os, sys


def get_node_info():
    """
	Returns the Node information from the running system
	"""
    return ("Node: " + platform.node())

def get_cpu_info():
    """
	Returns the CPU info from the running system
	"""
    print("Processors: ")
    with open("/proc/cpuinfo", "r")  as f:
        info = f.readlines()

    cpuinfo = [x.strip().split(":")[1] for x in info if "model name"  in x]
    for index, item in enumerate(cpuinfo):
        return ("    " + str(index) + ": " + item)

def get_memory_info():
    """
	Returns the Memory info from the running system
	"""
    with open("/proc/meminfo", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

def get_linux_version():
    """
	Returns the Linux Distribution Version from the running system
	"""
    dist = platform.dist()
    dist = " ".join(x for x in dist)
    return ("OS: " + platform.system() + ", Distribution: " + dist + "System: ")

def get_uptime_info():
    """
	Returns the Machine uptime information from the running system
	"""
    uptime = None
    with open("/proc/uptime", "r") as f:
        uptime = f.read().split(" ")[0].strip()
    uptime = int(float(uptime))
    uptime_hours = uptime // 3600
    uptime_minutes = (uptime % 3600) // 60
    return ("System Uptime: " + str(uptime_hours) + ":" + str(uptime_minutes) + " hours")

def get_providing_power_source_type(self):
    """
    Returns the Power Source information from the running system
	"""
    for supply in os.listdir(POWER_SUPPLY_PATH):
        supply_path = os.path.join(POWER_SUPPLY_PATH, supply)
        try:
            type = self.power_source_type(supply_path)
            if type == common.POWER_TYPE_AC:
                if self.is_ac_online(supply_path):
                    return common.POWER_TYPE_AC
            elif type == common.POWER_TYPE_BATTERY:
                if self.is_battery_present(supply_path) and self.is_battery_discharging(supply_path):
                    return common.POWER_TYPE_BATTERY
        except (RuntimeError, IOError) as e:
            warnings.warn("Unable to read properties of {0}: {1}".format(supply_path, e), category=RuntimeWarning)
    return common.POWER_TYPE_AC

# GPU Info
# lspci -vnn | grep VGA -A 12
# lspci


if __name__ == "__main__":
    print (get_linux_version())
    print (get_node_info())
    print (get_memory_info())
    print (get_cpu_info())
    print (get_uptime_info())
    
