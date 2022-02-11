class Unknow_Detector:
    def __init__(self):
        self.count = 0
        self.sequence = 0

    def set_count(self):
        self.count += 1

    def resset(self):
        self.count = 0
        self.count = 0

    def set_unknow(self):
        self.count += 1
        self.sequence += 1

    def set_sequence(self):
        self.sequence += 1

    def check_sequence(self):
        if self.count == self.sequence:
            self.count += 1
            self.sequence += 1
            return True
        else:
            self.count = 0
            self.sequence = 0
            return False

    def get_count(self):
        return self.count