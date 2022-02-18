import argparse
import os


class DefaultToEnvironment(argparse.Action):
    # taken from following:
    # - https://gist.github.com/orls/51525c86ee77a56ad396
    # - https://newbedev.com/setting-options-from-environment-variables-when-using-argparse

    def __init__(self, key: str, required: bool = True, default=None, **kwargs):
        # TODO: double check / simplify logic
        if not default and key:
            if key in os.environ:
                default = os.environ[key]
        if required and default:
            required = False
        super().__init__(default=default, required=required, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)


def default_to_env(key: str):
    return lambda **kwargs: DefaultToEnvironment(key, **kwargs)
