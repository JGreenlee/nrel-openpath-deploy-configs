import os
import sys
import json


def get_config_file_path(deployment):
    return f'configs/{deployment}.nrel-op.json'


def read_config(deployment):
    config_file_path = get_config_file_path(deployment)
    if not os.path.exists(config_file_path):
        print(f"There is no deployment called {deployment} - no changes made.")
        sys.exit(1)
    with open(config_file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def update_config(deployment, new_config, msg):
    config_file_path = get_config_file_path(deployment)
    if new_config and msg:
        with open(config_file_path, 'w', encoding='utf-8') as f:
            json.dump(new_config, f, indent=4, ensure_ascii=False)
        with open('/tmp/commit_message.txt', 'w') as f:
            f.write(f"`{deployment}`: {msg}")
        print(f"Updated {config_file_path} with new config.")
    else:
        print("No changes made.")
