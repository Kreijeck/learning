import os
import shutil
import py7zr
import tarfile
import zipfile
import logging

def add_logger():
    # create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    fh = logging.FileHandler("copy_files.log")
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s: %(name)s - %(levelname)s - %(message)s', "%Y -%m -%d %H:%M:%S")

    # add formatter to ch
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


# Add Logger for whole file
logger = add_logger()

def cleanup_workspace(all_dirs:list):
    for dir in all_dirs:
        if os.path.isdir(dir):
            shutil.rmtree(dir)
            logger.debug("{} has been removed recursivly".format(dir))
        else:
            logger.debug("No usage in cleanup, {} doesn't exist".format(dir))

def remove_old_zipped_files(filename, endings: list):
    for ending in endings:
        compl_filename = filename + "." + ending
        if os.path.isfile(compl_filename):
            os.remove(compl_filename)
            logger.debug("{} has been removed".format(compl_filename))
        else:
            logger.debug("{} doesn't exist and don't have to be removed".format(compl_filename))

def extract_files(path: str, to_directory="temp"):
    """
    Can extract .7z, .tar.gz, .zip
    :return path where files are extracted
    """
    if path.endswith('.tar.gz'):
        opener, mode = tarfile.open, 'r:gz'
    elif path.endswith('.7z'):
        opener, mode = py7zr.SevenZipFile, 'r'
    elif path.endswith('.zip'):
        opener, mode = zipfile.ZipFile, 'r'
    else:
        raise ValueError("Could not extract {}, bacause no extractor is found".format(path))

    # create absolute path of directory, where zips are saved
    cwd = os.getcwd()
    zip_dir = os.path.join(cwd, to_directory)
    try:
        file = opener(path, mode=mode)
        file.extractall(path=to_directory)
        logger.debug("File {} extracted".format(path))
    except FileNotFoundError:
        print("Can't extract {}, file doesn't exist".format(path))

    return zip_dir

def zip_folder(zip_mode: str, folder_path):

    if zip_mode == "tar.gz":
        opener, mode = tarfile.open, 'w:gz'
    elif zip_mode == "7z":
        opener, mode = py7zr.SevenZipFile, 'w'
    elif zip_mode == "zip":
        opener, mode = zipfile.ZipFile, 'w'
    else:
        raise ValueError("The mode {} wasn't supported to zip a File, only tar.gz, 7z, zip are available".format(zip_mode))

    zip_name = folder_path + "." + zip_mode
    zip_handler = opener(zip_name, mode)

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for file in filenames:
            if zip_mode == "tar.gz":
                zip_handler.add(os.path.join(dirpath, file), os.path.relpath(os.path.join(dirpath, file)))
            else:
                zip_handler.write(os.path.join(dirpath, file), os.path.relpath(os.path.join(dirpath, file)))


def create_folder_structure(folder_dict):
    """

    :param folder_dict: dictionary with all folders: folders with names keys, files as list
    :return:
    """
    rootdir = "augmented"
    for parent in folder_dict.keys():
        if type(folder_dict[parent]) is list:
            for child in folder_dict[parent]:
                folder_path = f"{rootdir}/{parent}/{child}"
                os.makedirs(folder_path)


def copy_template_folder(inputpath, outputpath):

    if os.path.isdir(outputpath):
        shutil.rmtree(outputpath)

    for dirpath, dirnames, filenames in os.walk(inputpath):
        rel_path_to_root = os.path.relpath(dirpath, inputpath)
        structure = os.path.join(outputpath, rel_path_to_root)

        # Copy Directories
        if not os.path.isdir(structure):
            logger.debug("Create folder: {}".format(structure))
            os.mkdir(structure)
        else:
            logger.warning("folder {} already exists".format(structure))

        # Copy Files
        for file in filenames:
            logger.debug("{} has been add in {}\\{}".format(file, outputpath, rel_path_to_root))
            src = os.path.join(inputpath, rel_path_to_root, file)
            dst = os.path.join(outputpath, rel_path_to_root, file)
            shutil.copy(src, dst)

    return outputpath


def get_all_files(path):
    all_files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            all_files.append(file)
    logger.debug("{} has been found in {}".format(all_files, path))
    return all_files

def file_mapping():
    # Filename: rename in, relative path
    fm = {"ArBaseExecutable.txt": ["Augbase.txt", "AugBase\\bin"],
          "ArVideoExecutable.txt": ["AugVideo.txt", "AugVideo\\bin"],
          "base_settings.txt": ["base_settings.txt", "AugBase\\config"],
          "video_settings.txt": ["video_settings.txt", "AugVideo\\config"],
          "libPose.txt": ["libPose.txt", "AugBase\\lib"]}

    logger.debug("Active Mapping orig_name: [rename_in, dst_path]: {}".format(fm))

    return fm


def move_binaries_to_template(src_path, dst_path):
    fm = file_mapping()
    for file in get_all_files(src_path):
        for file_key in fm.keys():
            if file_key == file:
                #rename file: pos 0
                name = fm[file][0]
                folder = fm[file][1]
                src = os.path.join(src_path, file)
                dst = os.path.join(dst_path, folder, name)
                if os.path.isfile(src):
                    logger.debug("{} has been moved to {}".format(src, dst))
                    shutil.move(src, dst)
                else:
                    logger.debug("{} doesn't exist".format(src))

def run_copy_binaries():
    ### Parameter ###
    # Input
    downloaded_zip = "files.tar.gz"
    template_dir = "template_augmented"

    # Output
    temp_dir_unzip = "temp"
    augmented_dir = "augmented"
    result_zip = "tar.gz"

    # Loglevel can be set to logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR
    logger.setLevel(logging.DEBUG)

    # download_gcc93
    # post cleanup
    cleanup_workspace([augmented_dir, temp_dir_unzip])
    remove_old_zipped_files(filename=augmented_dir, endings=["tar.gz", "zip", "7z"])

    path_unzip = extract_files(path=downloaded_zip, to_directory=temp_dir_unzip)
    augmented_path = copy_template_folder(inputpath=template_dir, outputpath=augmented_dir)
    move_binaries_to_template(path_unzip, augmented_path)

    # check if path_unzip is empty
    if len(os.listdir(path_unzip)) == 0:
        zip_folder(result_zip, augmented_path)
        # pre cleanup
        cleanup_workspace([augmented_dir, temp_dir_unzip])
    else:
        logger.error("Not all extracted files, from {} has been moved to {}, plz check manually! "
                     "Zip and cleanup has been skipped!".format(path_unzip, augmented_path))
    logger.debug("-----------------------------------------EndScript-------------------------------------------")

if __name__ == '__main__':
    run_copy_binaries()