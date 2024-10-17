import hashlib
import os
import shutil

import logging

logger = logging.getLogger("iphotoimport")


class FileSystem:
    def __init__(self, forceCopy):
        self.forceCopy = forceCopy

    def safe_link_file(self, src, dst):
        assert os.path.exists(src), "%s didn't exist" % src

        if self.forceCopy:
            self.mkdir(dst)
            shutil.copy(src, dst)
            return

        if os.path.exists(dst):
            if self.is_file_same(src, dst):
                # Nothing to do
                return
            else:
                raise Exception(
                    "Destination file %s exists and not equal to %s" % (dst, src)
                )
        else:
            self.mkdir(dst)
            # Try to link the file
            try:
                os.link(src, dst)
            except:
                logger.debug("Hard link failed, falling back on copy")
                shutil.copy(src, dst)

    def is_file_same(self, f1, f2):
        return os.path.samefile(f1, f2) or self.md5_for_file(f1) == self.md5_for_file(
            f2
        )

    def md5_for_file(self, filename, block_size=2**20):
        with open(filename, "rb") as f:
            md5 = hashlib.md5()
            while True:
                data = f.read(block_size)
                if not data:
                    break
                md5.update(data)
        return md5.hexdigest()

    def mkdir(self, dir):
        try:
            os.makedirs(os.path.dirname(dir))
        except Exception:
            pass
