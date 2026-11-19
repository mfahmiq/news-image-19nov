"""news-image-20261119 entry: copy the infographic beside this file to the
output directory as entry.png. A plain byte copy, so both grader runs write
identical bytes. Python 3.13, standard library only, no network."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(HERE, "entry.png")
DST = os.path.join(OUT, "entry.png")
os.makedirs(OUT, exist_ok=True)
shutil.copyfile(SRC, DST)
assert os.path.getsize(DST) == os.path.getsize(SRC), "copy size mismatch"
print("entry.png:", os.path.getsize(DST), "bytes ->", DST)
