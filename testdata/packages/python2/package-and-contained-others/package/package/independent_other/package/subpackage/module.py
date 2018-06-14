from pysourceinfo import getcaller_module_name
class Cpkg(object):
    def getData(self,callback=None):
        if callback:
            cb = callback()
            return cb
        return getcaller_name()