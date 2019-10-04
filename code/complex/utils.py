from functools import partial


def to_int(value):
    return int(float(value))


def to_float(value):
    return float(value.replace(',', '.'))


def to_bool(value):
    return str(value).lower() in ('true', 'yes', 'si', 'y', 's', '1')


def catch_value(message=None, recursive=False, default=None, cast=None):
    if not isinstance(message, str):
        message = 'Por favor, ingrese un valor'
    else:
        message = message.strip()
    if not message.endswith(':'):
        message += ': '
    if default is not None:
        message =  '{} [{}]: '.format(message[:-2], str(default))
    value = input(message).strip()
    if default is not None and not value:
        return default
    if cast is not None:
        try:
            value = cast(value)
        except:
            if recursive is True:
                return catch_value(message, recursive, default, cast)
            raise ValueError('El valor ingresado no es correcto: ', value)
    return value


catch_int = partial(catch_value, cast=to_int)
catch_float = partial(catch_value, cast=to_float)
catch_bool = partial(catch_value, cast=to_bool)


def tbiter(traceback):
    while traceback:
        yield traceback
        traceback = traceback.tb_next


def tblast(traceback):
    return [x for x in tbiter(traceback)][-1]


def except_hook(exception, value, traceback):
    tb = tblast(traceback)
    if exception is not KeyboardInterrupt:
        print('')
        print('ERROR <{}>:'.format(exception.__name__))
        print('  > {}'.format(value))
        data = (tb.tb_frame.f_code.co_filename, tb.tb_lineno)
        print('  ! File {}, line {}'.format(*data))
        print('--')
    else:
        print('')
    print('Bye!')
    exit(-9)
