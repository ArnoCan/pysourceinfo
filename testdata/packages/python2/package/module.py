from pysourceinfo.objectinfo import getcaller_module_name,getcaller_name
class Cpkg(object):
    def getData(self,callback=None):
        if callback:
            cb = callback()
            return cb
        return getcaller_name()