import file_processing
from pathlib import Path
import logging
import shutil
import os

cwd = os.getcwd()
down = str(Path.home() / "Downloads")

def split():
    shutil.copyfile("C:\\Users\\ASUS\\Downloads\\noon.mp4",
                    cwd + "\\out\\out.mp4")

    fsplitter = file_processing.FileProcessor()

    #Set size of each chunk, for example: 25 mb
    p_size = 20

    #File to split and subdir where to save chunks
    from_file = cwd+"\\out\\out.mp4"
    to_dir = cwd+"\\out"

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

    if os.path.exists(cwd+"\\out\\out.mp4"):
        os.remove(cwd+"\\out\\out.mp4")

def join():
    fjoiner = file_processing.FileProcessor()

    #Set the size-value for reading chunks, for example: 25 mb
    readsize = 20

    #Set chunks dir and dest filename
    from_dir = cwd+"\\out"
    to_file = down+"\\output.mp4"

    absfrom, absto = map(os.path.abspath, [from_dir, to_file])
    print('Joining', absfrom, 'to', absto, 'by', readsize)
    #Join now
    fjoiner.join_file(from_dir, readsize, to_file)