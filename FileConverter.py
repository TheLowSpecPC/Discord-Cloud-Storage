import splitnjoin as snj
import os

def split():
    fsplitter = snj.FileProcessor()

    #Set size of each chunk, for example: 25 mb
    p_size = 20

    #File to split and subdir where to save chunks
    from_file = "D:\\Movies\\Leo (2023) Tamil HQ HDRip - 1080p.mkv"
    to_dir = "C:\\Users\\ASUS\\PycharmProjects\\Discord-Cloud-Storage\\out"

    absfrom, absto = map(os.path.abspath, [from_file, to_dir])
    print('Splitting', absfrom, 'to', absto, 'by', p_size, 'mb...')
    #Split now
    fsplitter.split_file_by_size(from_file, p_size, to_dir)

def join():
    fjoiner = snj.FileProcessor()

    #Set the size-value for reading chunks, for example: 25 mb
    readsize = 20

    #Set chunks dir and dest filename
    from_dir = "C:\\Users\\ASUS\\PycharmProjects\\Discord-Cloud-Storage\\out"
    to_file = "C:\\Users\\ASUS\\Downloads\\out.mkv"

    absfrom, absto = map(os.path.abspath, [from_dir, to_file])
    print('Joining', absfrom, 'to', absto, 'by', readsize)
    #Join now
    fjoiner.join_file(from_dir, readsize, to_file)