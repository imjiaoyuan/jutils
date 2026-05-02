import importlib


def _dispatch(module_name: str, func_name: str = "cmd"):
    def _runner(args):
        module = importlib.import_module(module_name)
        getattr(module, func_name)(args)

    return _runner
