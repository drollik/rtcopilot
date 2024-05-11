import os


class FileHandling:
    def __init__(self, rootdir):
        self.rootdir = rootdir  # where to start looking for python files
        self.weapon_files = []
        self.ams_files = []
        self.ammo_files = []
        self.EXCLUDE = ['Melee', 'FCS', 'Linked', 'Turret',
                        'Ambush', 'Infantry', 'deprecated',
                        'Quirk', 'quirk', 'Nuke']

    def initialize(self):
        """
            All:
                file has "json" in name (endswith ".json"?)
                file has NOT self.EXCLUDE in name
            Weapons:
                file has "Weapons_" in name
                file has NOT "AMS" in name
            Ams:
                file has "Weapons_" in name
                file has "AMS" in name
            Ammo:
                file has "Ammunition_" in name
        """

        print("in initialize()")
        # weapons and ams
        for dirpath, dirnames, filenames in os.walk(self.rootdir):
            for filename in filenames:
                if filename.endswith(".json"):
                    if any(x in filename for x in self.EXCLUDE):
                        # print(f"XXX excluded: {filename}")
                        pass
                    else:
                        # none of the excluded match
                        if 'Weapon_' in filename:  # must have "Weapon_" in filename
                            if 'AMS' in filename:
                                # it's an ams
                                self.ams_files.append(os.path.join(dirpath, filename))
                                print(filename)
                            else:
                                # it's a weapon
                                self.weapon_files.append(os.path.join(dirpath, filename))
                        elif 'Ammunition_' in filename:
                            # it's ammo
                            self.ammo_files.append(os.path.join(dirpath, filename))

        print(f"found {len(self.weapon_files)} weapons")
        print(f"found {len(self.ams_files)} ams")
        print(f"found {len(self.ammo_files)} munitions")

    def __str__(self):
        return f"FileHandling(root={self.rootdir})"


if __name__ == "__main__":
    fh = FileHandling(r"C:\RogueTech\RtlCache")
    fh.initialize()
