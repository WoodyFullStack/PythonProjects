class SuperParentClass:
    def print_hello(self, argument):
        print(argument)


class my_first_class(SuperParentClass):
    """This class about public and private attributes"""
    x = 1
    _y = 2
    __z = 3

    def get_z(self):
        print(self.__z)

    @property
    def y(self):
        return self._y


my_first_object = my_first_class()
# print public class attribute
print(my_first_object.x)
# print protected class attribute
print(my_first_object.y)
# try to print private class attribute - it's impossible
try:
    print(my_first_object.z)
except AttributeError:
    print("AttributeError raised. You can't print 'z', because it's private")

my_first_object.print_hello("Print method called from SuperParentClass")
