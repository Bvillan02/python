class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        self.__status = not self.__status
        if not self.__status:
            self.__muted = False

    def mute(self):
        #Fix ME
        if self.__status:
            self.__muted = not self.__muted


    def channel_up(self):
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self):
        if self.__status:
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self):
        if self.__status and not self.__muted:
            self.__volume = min(self.__volume + 1, self.MAX_VOLUME)

    def volume_down(self):
        if self.__status and not self.__muted:
            self.__volume = max(self.__volume - 1, self.MIN_VOLUME)

    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'