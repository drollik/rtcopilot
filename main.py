import sys
import filehandling
import weapon


if __name__ != "__main__":
    print("NOT in main")
    sys.exit(-1)
else:
    print("Welcome to RT-CoPilot")

    fh = filehandling.FileHandling(r'C:\RogueTech\RtlCache\RtCache')
    # print(fh.weapon_files)

    # WEAPONS
    print(f"found {len(fh.weapon_files)} weapons")
    # AMS
    print(f"found {len(fh.ams_files)} ams")
    # MUNITIONS
    print(f"found {len(fh.ammo_files)} munitions")

    # print(self.weapon_files, sep="\n")
    some = [i for i in fh.weapon_files if 'MediumLaser' in i]
    # print(*some, sep="\n")

    for f in fh.ams_files:
        print(f)
        # w = weapon.Weapon(f)
        # print(w.to_json())
        # print(w.data) # print raw
