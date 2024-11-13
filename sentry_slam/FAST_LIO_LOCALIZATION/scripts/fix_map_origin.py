#!/home/yanzj/anaconda3/envs/navigation/bin/python
# coding=utf8
import yaml
import math
import argparse
import os
import time

def fix_nan_in_origin(yaml_file_path):
    while not os.path.exists(yaml_file_path):
        print(f"Waiting for {yaml_file_path} to be created...")
        time.sleep(0.1)

    with open(yaml_file_path, 'r') as file:
        data = yaml.safe_load(file)
    origin = data.get('origin', None)
    if origin and len(origin) == 3:
        try:
            origin = [float(origin[0]), float(origin[1]), float(origin[2])]
            if math.isnan(origin[2]):
                origin[2] = 0
                print(f"Fix successful: origin[2] was NaN, set it to 0.")
            else:
                print("No fix needed: origin[2] is not NaN.")
        except ValueError:
            if origin[2] == "-nan":
                origin[2] = 0
                print("Fix successful: origin[2] was '-nan', set it to 0.")
            else:
                print("Error: origin[2] is not a valid number, cannot fix.")
        data['origin'] = origin
    else:
        print("Error: 'origin' is missing or its length is not 3, cannot fix.")
    class FloatDumper(yaml.SafeDumper):
        def represent_float(self, data):
            if data == int(data):
                return self.represent_int(int(data))
            return super().represent_float(data)
    with open(yaml_file_path, 'w') as file:
        yaml.dump(data, file, Dumper=FloatDumper, default_flow_style=None)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fix NaN in YAML origin field.")
    parser.add_argument('yaml_file', type=str, help="Path to the YAML file.")
    args, unknown = parser.parse_known_args()
    fix_nan_in_origin(args.yaml_file)
