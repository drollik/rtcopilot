import sys
import filehandling

if __name__ != "__main__":
    print("NOT in main")
    sys.exit(-1)
else:
    print("Welcome to RT-CoPilot")

    fh = filehandling.FileHandling(r"'C:\RogueTech\RtlCache'")
    print(fh)
