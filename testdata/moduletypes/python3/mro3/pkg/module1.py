class CModule1(object):
    def getData(self,callback):
        if callback:
            cb = callback()
            return cb
