import sys
import urllib

_handy_args = sys.argv[1:]


def pop_arg_int():
    if not _handy_args:
        return None

    i = _handy_args.pop(0)
    return int(i)


def pop_arg_str():
    if not _handy_args:
        return None

    return _handy_args.pop(0)


def parse_path(p):
    """
    :param p: is a HTTP path like "/foo?parameter=value&other=some"
    :return: tuple with first part is plain path ("foo") and a dictionary of parameters.
    """
    pos = p.find('?')
    if pos < 0:
        path = p
        args = dict()
    else:
        path = p[0:pos]
        args = urllib.parse.parse_qs(p[pos + 1:])  # parse foo=bar&zip=doo into a dict

    dict_one_value_mutate(args)
    return path, args


def dict_one_value_mutate(d):
    """If a dictionary key has one value in an array, mutate the value to be just the value.

    For example, input: {'foo': ['bar']}
    output: {'foo': 'bar'}
    """

    for k, v in d.items():
        if isinstance(v, (list, tuple)) and len(v) == 1:
            d[k] = v[0]
