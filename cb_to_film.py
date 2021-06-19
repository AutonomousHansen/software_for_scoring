#!/usr/bin/env python
import os
import fnmatch, string
import re

#List of instrument keys

abbr_dict = {
    ('pic', 'fl', 'afl', 'ob', 'eh', 'cl', 'bcl', 'bsn') : 'WW', 
    ('fh', 'tpt', 'tbn', 'btbn', 'tb') : 'BRS',
    ('timp', 'cym', 'gc', 'bd', 'xyl', 'mrb', 'glk', 'vib', 'tbls', 'hprc', 'sprc') : 'PRC',
    ('pno', 'clst', 'epno', 'org', 'hrp') : 'KBHRP',
    ('vln', 'vla', 'vc', 'cb') : 'STR',
    ('svx', 'choir') : 'VC',
    ('egt', 'agt') : 'GUIT',
    ('kd', 'sn', 'cym', 'hh', 'tom', 'loop') : 'DRUMS',
    ('ebs', 'sbs') : 'BASS',
    ('synth') : 'SYN'
}

def format_string(abbr, filename):
    bp = filename.split("_")
    return bp[0] + "_{}_".format(abbr) + bp[1]

def main():
    files = [f for f in os.listdir(os.getcwd()) if fnmatch.fnmatch(f, '[!_]*')]
    for f in files:
        try:
            inst = re.findall(r'(?!=)([a-z1-9]*)(?=.wav)', f)[0].strip(string.digits)
            for keys, abbr in abbr_dict.items():
                if abbr in f:
                    print ("Named already processed")
                    continue
                if str(inst) in set(keys):
                    new_name = format_string(abbr, f)
                    print(new_name)
                    os.rename(f, new_name)
        except:
            print("Couldn't handle file {}".format(f))
            continue

if __name__ == "__main__":
    # execute only if run as a script
    main()