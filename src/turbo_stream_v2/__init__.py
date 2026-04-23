import json
import os
import pathlib
import subprocess

from nodejs_wheel.executable import ROOT_DIR as NODE_ROOT_DIR

NODE_EXE = "node.exe" if os.name == "nt" else "node"
NODE_PATH = pathlib.Path(NODE_ROOT_DIR) / NODE_EXE
INDEX_JS = pathlib.Path(__file__).parent / "js" / "index.ts"


def decode(data_input: bytes):
    proc = subprocess.Popen(
        [NODE_PATH, INDEX_JS],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    stdout, stderr = proc.communicate(input=data_input)

    if proc.returncode != 0:
        raise RuntimeError(stderr.decode("utf-8"))

    result = json.loads(stdout.decode("utf-8"))

    return result
