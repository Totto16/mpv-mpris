#!/usr/bin/env python3

import sys
import json
import pathlib

file: pathlib.Path = pathlib.Path(sys.argv[1])
assert file.exists()

with open(file, "r", encoding="utf-8") as f:
    data = f.read()

c_name = file.stem.replace(".", "_").upper()

print(f"#define {c_name} {json.dumps(obj=data)}")
