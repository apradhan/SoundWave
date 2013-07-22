class SnapRec:
        def __init__(self, row, snapid, volume_id, description, start_time):
                self.row = row
                self.snapid = snapid
                self.volume_id = volume_id
                self.description = description
                self.start_time = start_time
        def __repr__(self):
                return repr((self.row, self.snapid, self.volume_id, self.description, self.start_time))