# The BackingPhotoTable
#                  id = 1
#            filepath = /home/shaun/Pictures/Photos/2008/03/24/DSCN2416 (Modified (2))_modified.JPG
#           timestamp = 1348968706
#            filesize = 1064375
#               width = 1600
#              height = 1200
# original_orientation = 1
#         file_format = 0
#        time_created = 1348945103

class BackingPhotoTable:
    def __init__(self, db):
        self.db = db
        self.init()

    def insert(self, photo):
        cursor = self.db.execute("""
                    INSERT INTO BackingPhotoTable (filepath,
                                                   timestamp,
                                                   filesize,
                                                   width,
                                                   height,
                                                   original_orientation,
                                                   file_format,
                                                   time_created)
                    VALUES (:new_mod_path,
                            :mod_timestamp,
                            :mod_file_size,
                            :mod_width,
                            :mod_height,
                            :mod_original_orientation,
                            :file_format,
                            :time_created)
                """, photo)
        return cursor.lastrowid


    def init(self):
        cursor = self.db.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='BackingPhotoTable'")
        if (cursor.fetchone()[0] == 0):
            self.db.execute("CREATE TABLE BackingPhotoTable ("
                                "id INTEGER PRIMARY KEY, "
                                "filepath TEXT UNIQUE NOT NULL, "
                                "timestamp INTEGER, filesize INTEGER, "
                                "width INTEGER, "
                                "height INTEGER, "
                                "original_orientation INTEGER, "
                                "file_format INTEGER, "
                                "time_created INTEGER "
                            ")")
