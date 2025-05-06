import os
import shutil
import tempfile

with tempfile.TemporaryDirectory() as tmpdir:
    new_dir = os.path.join(tmpdir, "my_folder")
    os.makedirs(new_dir)
    print(f"Created: {new_dir}")

    shutil.rmtree(new_dir)
    print(f"Deleted: {new_dir}")
