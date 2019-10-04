from functools import partial


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


def int_helper(value):
	return int(float_helper(value))


def float_helper(value):
	return float(value.replace(',', '.'))


def bool_helper(value):
	return str(value).lower() in ('true', 'yes', 'si', 'y', 's', '1')


catch_int = partial(catch_value, cast=int_helper)
catch_float = partial(catch_value, cast=float_helper)
catch_bool = partial(catch_value, cast=bool_helper)
