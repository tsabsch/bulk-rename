import argparse
from datetime import datetime
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)


parser = argparse.ArgumentParser()
parser.add_argument("dir", type=str)
parser.add_argument("--oldformat", type=str, required=True)
parser.add_argument("--newformat", type=str, required=True)
args = parser.parse_args()


files = [f for f in Path(args.dir).iterdir() if f.is_file()]

for f in files:
    try:
        d = datetime.strptime(f.stem, args.oldformat)
    except ValueError:
        logging.info(f"Skipping {f.name}: Not matching the date format")
        continue
        
    new_name = d.strftime(args.newformat) + f.suffix
    logging.info(f"Renaming {f.name} -> {f.parent / new_name}")
    f.rename(f.parent / new_name)

