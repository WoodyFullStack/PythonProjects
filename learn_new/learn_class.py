
class my_first_class:
    """This class about public and private attributes"""
    x = 1
    _y = 2
    __z = 3

    def get_z(self):
        print(self.__z)

    def set_z(self, z):
        __z = z



my_first_object = my_first_class()
# print public class attribute
print(my_first_object.x)
# print protected class attribute
print(my_first_object._y)
# try to print private class attribute - it's impossible
try:
    print(my_first_object.z)
except AttributeError:
    print("AttributeError raised. You can't print 'z', because it's private")

my_first_object.get_z()
my_first_object.set_z(4)
my_first_object.get_z()