# packager
# package the files to be sent

import os
import time
import gzip
import shutil
import zipfile
# Usage: Compress a single file
# Arguments: filename
# Return Value: compressed filename
# Side effect: update files.db entry
# Notes:
def compress_single_file(filename):
    with zipfile.ZipFile(filename + '.zip', 'w') as myzip:
        myzip.write(filename)
    pass



# Usage: Compress multiple files
# Arguments: list of file name
# Return Value: compressed filename
# Side effect: None
# Notes: Should only be used prior to transfering multiple files together
def compress_multiple_file(li_filename):
    timestamp = str(time.time())
    with zipfile.ZipFile(timestamp + '.zip', 'w') as myzip:
        for name in li_filename:
            myzip.write(name)

    return timestamp + '.zip'
    pass


# Usage: Compress multiple files
# Arguments: list of file name
# Return Value: compressed filename
# Side effect: None
# Notes: Should only be used prior to transfering multiple files together
def zipdir(path):
    timestamp = str(time.time())
    ziph = zipfile.ZipFile(timestamp + '.zip', 'w', zipfile.ZIP_DEFLATED)
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

    ziph.close()
    return timestamp + '.zip'

# Usage: extract compressed file
# Arguments: filename of the compressed file
# Return Value: None
# Side effect: None
# Notes: Should only be used after receiving the transfered files
def unzip_file(compressed_filename):
    myzip = zipfile.ZipFile(compressed_filename)
    myzip.extractall()
    pass



