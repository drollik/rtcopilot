import json
import sys

class Weapon:
    def __init__(self, filename):
        self.filename = filename  # the file this weapon is stored in
        # self.file = None
        self.data = None
        self.initialize()

    def initialize(self):
        with open(self.filename, 'r') as self.file:
            try:
                self.data = json.load(self.file)
            except:
                print(f'Exception parsing {self.filename}, ignoring!')
    def __str__(self):
        return f"Weapon(file={self.filename})"

    def to_json(self):
        # print("size: ", len(self.data))
        return json.dumps(self.data, indent=2)
        # for key, value in self.data.items():
        #     print(f'{key}: {value}')


if __name__ == "__main__":
    filenames = [
        r'C:\RogueTech\RtlCache\RtCache\Core\RogueModuleTech\Weapons\Weapon_Autocannon_AC_2.json',
        r'C:\RogueTech\RtlCache\RtCache\Core\RogueModuleTech\Weapons\Weapon_Autocannon_AC_5.json',
        r'C:\RogueTech\RtlCache\RtCache\Core\RogueModuleTech\Weapons\Weapon_Autocannon_AC_10.json',
        r'C:\RogueTech\RtlCache\RtCache\Core\RogueModuleTech\Weapons\Weapon_Autocannon_AC_20.json',
        r'C:\RogueTech\RtlCache\RtCache\Core\RogueModuleTech\Clan\Improved\Weapon_Autocannon_AC_10_CE.json',
        r'C:\RogueTech\RtlCache\RtCache\Core\RogueModuleTech\Weapons\Weapon_Laser_Small.json',
        r'C:\RogueTech\RtlCache\RtCache\Core\RogueModuleTech\Weapons\Weapon_Laser_Medium.json',
        r'C:\RogueTech\RtlCache\RtCache\Core\RogueModuleTech\Weapons\Weapon_Laser_Pulse_Medium.json',
        r'C:\RogueTech\RtlCache\RtCache\Core\RogueModuleTech\Weapons\Weapon_LRM_10.json'
    ]
    for f in filenames:
        w = Weapon(f)
        # print(w)        # type and filename only
        print(w.data)   # string on one line
        # print(w.to_json())
