#!/usr/bin/env python
import os
import fnmatch, string
import regex as re

#List of instrument keys

abbr_dict = {
    ('pic', 'fl', 'afl', 'ob', 'eh', 'cl', 'bcl', 'bsn') : 'WW', 
    ('fh', 'tpt', 'tbn', 'btbn', 'tb') : 'BRS',
    ('timp', 'sn', 'cym', 'gc', 'bd', 'xyl', 'mrb', 'glk', 'vib', 'tbls', 'hprc', 'sprc') : 'PRC',
    ('pno', 'clst', 'epno', 'org', 'hrp') : 'KBHRP',
    ('vln', 'vla', 'vc', 'cb') : 'STR',
    ('svx', 'choir') : 'VC',
    ('egt', 'agt') : 'GUIT',
    ('kd', 'sn', 'cym', 'hh', 'tom', 'loop') : 'DRUMS',
    ('ebs', 'sbs', 'cb') : 'BASS',
    ('synth') : 'SYN'
}

def format_string(abbr, filename):
    bp = filename.split("_")
    return bp[0] + "_{}_".format(abbr) + bp[1]

def main():
    files = [f for f in os.listdir(os.getcwd()) if fnmatch.fnmatch(f, '[!_]*')]
    for f in files:
        inst = re.findall(r'(?!=)([a-z1-9]*)(?=.wav)', f)
        for keys, abbr in abbr_dict.items():
            if str(inst) in set(keys):
                new_name = format_string(abbr, f)
                os.rename(f, new_name)

if __name__ == "__main__":
    # execute only if run as a script
    main()