class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2

    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

# overall, it was pretty accurate. you just had some logic issues in the volume functions
# You were also missing some "-> None" in your functions (it doesn't affect the code,
    # it's just for documentation purposes)

    def __init__(self) -> None:
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to power television on and off
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Method to mute television
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Method to increase television channel
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel = self.__channel + 1
            else:
                self.__channel = Television.MIN_CHANNEL


    def channel_down(self) -> None:
        """
        Method to decrease television channel
        """
        # You had an extra if self.__status here and it wasn't needed
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel = self.__channel - 1
            else:
                self.__channel = Television.MAX_CHANNEL


    def volume_up(self) -> None:
        """
        Method to turn television volume up
        """
        # You had a logic issue here that was messing up the Volume output
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume = self.__volume + 1

    def volume_down(self) -> None:
        """
        Method to turn television volume down
        """
        # You had a logic issue here that was messing up the Volume output
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume = self.__volume - 1

# you forgot to add "-> str" to specify that the return value will be a string. as previously mentioned, it doesn't
# affect the code
    def __str__(self) -> str:
        """
        Method to show television status
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
