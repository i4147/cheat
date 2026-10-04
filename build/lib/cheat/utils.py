from __future__ import print_function
import sys
class Utils:
    @staticmethod
    def die(message):
        Utils.warn(message)
        exit(1)
    @staticmethod
    def warn(message):
        print((message), file=sys.stderr)
    @staticmethod
    def boolify(value):
        if not isinstance(value, str):
            return value
        return value.strip().lower() == "true"
