#!/bin/bash
rosrun map_server map_saver map:=/projected_map -f $1
rosrun fast_lio_localization fix_map_origin.py $1.yaml
