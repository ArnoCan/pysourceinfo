from __future__ import absolute_import

#
#######################
#
class Dummy1(object):

    myName = "Dummy1"

    def __init__(self):
        pass

    def set(self,a):
        self.a = a

    def get(self):
        return self.myName+str(self.a)
