#!/usr/bin/env python3

import json
import os

def get_logs_json():
    logdir = "logs/"
    logfiles = os.listdir(logdir)
    logfiles.sort()
    stats_list = []
    for filename in logfiles:
        with open(logdir + filename, 'r') as f:
            firstline = f.readline().rstrip()
            start_time, cmdline = firstline.split(" I  (CXR ARCore)  Parsing commandline string: ")
            server_addr, si, nic, nt = cmdline.split()[1::2]

            stat_list = []
            for line in f.readlines():
                stat_timestamp, stat_str = line.rstrip().split(" I  (CXR ARCore)  cxrConnectionStats ")
                stat = json.loads(stat_str)
                stat["timestamp"] = stat_timestamp
                stat_list.append(stat)

            if len(stat_list) > 0:
                stat_obj = {}
                stat_obj["measurement_id"] = filename.split(".txt")[0]
                stat_obj["server"] = server_addr
                stat_obj["nic"] = nic
                stat_obj["nt"] = nt
                stat_obj["ideal_interval"] = si
                stat_obj["start_time"] = start_time
                stat_obj["stats"] = stat_list
                stats_list.append(stat_obj)
    return stats_list

if __name__ == '__main__':
    stats_list = get_logs_json()
    with open("out.json", "w") as f:
        json.dump(stats_list, f, indent=2)
