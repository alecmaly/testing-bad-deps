#!/usr/bin/python3

import sys
import json
import requests

if len(sys.argv) != 3:
    print(f"Usage: python3 {sys.argv[0]} <repo_url> <package.json>")
    print(f"Example: python3 {sys.argv[0]} 'https://registry.npmjs.org/' package.json")
    print("NOTE: Can use command `npm config get registry` to get url to current registry.")
    sys.exit()

repo_base_url = sys.argv[1]
package_json_filepath = sys.argv[2]

f = open(package_json_filepath)
data = json.loads(f.read())

for name in data:
    if "dependencies" in name.lower(): 
        print(f"\n[+] Checking: {name}")
        dependencies = data[name]
        for dependency in dependencies:            
            url = f"{repo_base_url}{dependency}"
            resp = requests.get(url)
            if resp.status_code != 200:
                print(f"[{resp.status_code}]\t{dependency.ljust(45)} ({dependencies[dependency]}): {url}")