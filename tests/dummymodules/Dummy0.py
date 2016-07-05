from __future__ import absolute_import

#
#######################
#
class Dummy0:

    myName = "Dummy0"
    
    def __init__(self):
        pass

    def set(self,a):
        self.a = a

    def get(self):
        return self.myName+str(self.a)
