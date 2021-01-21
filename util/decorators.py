from functools import wraps


def osc_message():
    def decorator(func):
        def unzip(translate, value):
            return dict(zip(translate, value))

        def parse_osc_path(path) -> dict:
            path = path.split("/")
            parsed = unzip(['group', 'item', 'id'], path[1:4])
            if len(path) == 5: parsed['sub_id'] = path[4]
            return parsed

        @wraps(func)
        def parse_osc_message(*args, **kwargs):
            args = list(args)
            kwargs.update(unzip(['ip', 'port'], args.pop(0)))
            message = (parse_osc_path(args.pop(0)))
            if len(args) != 0: message['value'] = args.pop(0)
            kwargs['group'] = message.pop('group')
            kwargs['message'] = message
            print(f'osc returning {args}, {kwargs}')
            return func(*args, **kwargs)

        return parse_osc_message

    return decorator


def app_message_hacks():
    def decorator(func):
        def all_nothing_fader_buttons(message):
            if 'item' in message:
                if message['item'] in ['max', 'zero']:
                    new_value = 0
                    if message['item'] == 'max': new_value = 255
                    message['item'] = ['', 'red', 'green', 'blue', 'intensity'][int(message['value'])]
                    message['value'] = new_value
                return message

        @wraps(func)
        def apply_message_hacks(*args, **kwargs):
            if 'message' in  kwargs:
                message = kwargs['message']
                if len(message) > 0:
                    kwargs['message'] = all_nothing_fader_buttons(message)
            return func(*args, **kwargs)

        return apply_message_hacks

    return decorator



