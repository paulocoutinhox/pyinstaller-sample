class API:
    def call(self, func, params=None):
        # func = 'mypackage.mymodule.myfunc'
        # params = any or none
        import importlib

        mod_name, func_name = func.rsplit(".", 1)
        mod = importlib.import_module(mod_name)
        importlib.reload(mod)
        func_obj = getattr(mod, func_name)

        if params:
            return func_obj(params)
        else:
            return func_obj()
