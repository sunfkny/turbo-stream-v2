import json
import pathlib
import pprint

import turbo_stream_v2

PWD = pathlib.Path(__file__).parent

OUTPUT_DIR = PWD / "output"
OUTPUT_DIR.mkdir(exist_ok=True)
DATA_DIR = PWD / "data"

for test_case in DATA_DIR.iterdir():
    print("=" * 80)
    print("Test case:", test_case.absolute())

    data_input = test_case.read_bytes()

    result = turbo_stream_v2.decode(data_input)

    print("Result Preview:", pprint.pformat(result, depth=2))
    output = OUTPUT_DIR / f"{test_case.stem}.json"
    output.write_text(json.dumps(result, indent=2))
    print("Full result:", output.absolute())
