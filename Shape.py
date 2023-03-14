import  abc
class Shape(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def chuVi(self):
        pass

    @abc.abstractmethod
    def dienTich(self):
        pass


