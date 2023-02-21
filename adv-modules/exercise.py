import os
import shutil
import re

if __name__ == "__main__":
    cur_dir = os.getcwd()
    inst_file = os.path.join(cur_dir, "unzip_me_for_instructions.zip")
    archive = os.path.join(cur_dir, "extracted_content")

    if not os.path.isfile(archive):
        shutil.unpack_archive(inst_file)

    for dirpath, _, files in os.walk(archive):
        for file in files:
            with open(os.path.join(archive, dirpath, file)) as f:
                fdata = f.read()
                for num in re.findall(r"\d{3}-\d{3}-\d{4}", fdata):
                    print(num)
