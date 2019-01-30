from abc import ABCMeta, abstractmethod


class Girls(metaclass=ABCMeta):
    """
    This abstract class describes common methods to get information about lovely girls ;)
    """

    @abstractmethod
    def get_girl_name(self):
        pass

    @abstractmethod
    def get_girl_age(self):
        pass

    @abstractmethod
    def get_girl_fotos(self):
        pass

    @abstractmethod
    def get_working_girls(self):
        pass

    @abstractmethod
    def get_all_girls(self):
        pass

    @abstractmethod
    def get_girl_boobs(self):
        pass
