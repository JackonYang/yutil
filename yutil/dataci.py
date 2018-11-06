import json
import os


exclude_keys = [
    '#',  # comments
]


def use_data(data):
    def wrapper(f):
        def _func(*args, **kwargs):
            for tc in data:  # tc is short for testcase
                try:
                    if isinstance(tc, dict):
                        tc = {k: v for k, v in tc.items() if k not in exclude_keys}
                        f(**tc)
                    else:
                        f(*tc)
                except AssertionError:
                    print('AssertionError caused by testcase:\n%s' % json.dumps(tc, indent=4))
                    raise
        return _func
    return wrapper


def use_json_data(filename):
    def wrapper(f):
        def _func(request, *args, **kwargs):
            data_file = os.path.join(request.fspath.dirname, 'dt-data', filename)
            with open(data_file) as fp:
                try:
                    data = json.load(fp)
                except ValueError:
                    print('Not a valid JSON file: %s' % data_file)
                    raise

            for tc in data:
                try:
                    if isinstance(tc, dict):
                        tc = {k: v for k, v in tc.items() if k not in exclude_keys}
                        f(**tc)
                    else:
                        f(*tc)
                except AssertionError:
                    print('AssertionError caused by testcase:\n%s' % json.dumps(tc, indent=4))
                    print('in file: %s' % data_file)
                    raise
        return _func
    return wrapper
