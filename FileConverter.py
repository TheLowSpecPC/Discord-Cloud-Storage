import file_processing
from pathlib import Path
import logging
import shutil
import os

cwd = os.getcwd()
down = str(Path.home() / "Downloads")

def split(dir):
    file_tmp = dir.split("\\")[len(dir.split("\\")) - 1]
    file = file_tmp.split("/")[len(file_tmp.split("/")) - 1]

    if os.path.exists(cwd + f"\\out\\{file}\\"):
        pass
    else:
        os.mkdir(cwd + f"\\out\\{file}\\")

    shutil.copyfile(dir,
                    cwd + f"\\out\\{file}\\" + file)

    fsplitter = file_processing.FileProcessor()

    #Set size of each chunk, for example: 25 mb
    p_size = 20

    #File to split and subdir where to save chunks
    from_file = cwd + f"\\out\\{file}\\" + file
    to_dir = cwd + f"\\out\\{file}\\"

    if not os.path.exists(to_dir):
        try:
            os.mkdir(to_dir)
        except PermissionError as perm_err:
            logging.error(str(perm_err))
        except OSError as os_err:
            logging.error(str(os_err))

    absfrom, absto = map(os.path.abspath, [from_file, to_dir])
    print('Splitting', absfrom, 'to', absto, 'by', p_size, 'mb...')

    #Split now
    fsplitter.split_file_by_size(from_file, p_size, to_dir)

    if os.path.exists(cwd + f"\\out\\{file}\\" + file):
        os.remove(cwd + f"\\out\\{file}\\" + file)

def join(file):
    fjoiner = file_processing.FileProcessor()

    #Set the size-value for reading chunks, for example: 25 mb
    readsize = 20

    #Set chunks dir and dest filename
    from_dir = cwd + f"\\out\\{file}\\"
    to_file = down + "\\" + file

    absfrom, absto = map(os.path.abspath, [from_dir, to_file])
    print('Joining', absfrom, 'to', absto, 'by', readsize)
    #Join now
    fjoiner.join_file(from_dir, readsize, to_file)