MARKDOWN_SYMBOLS = '*_`'


def _rst(symbol, *content, sep=' '):
    start, end = (symbol, symbol) if isinstance(symbol, str) else (symbol[0], symbol[1])
    return start + sep.join(map(str, content)) + end


def text(*content, sep=' '):
    return _rst('', *content, sep)


def bold(*content, sep=' '):
    return _rst(MARKDOWN_SYMBOLS[0], *content, sep)


def italic(*content, sep=' '):
    return _rst(MARKDOWN_SYMBOLS[1], *content, sep)


def code(*content, sep=' '):
    return _rst(MARKDOWN_SYMBOLS[2], *content, sep)


def pre(*content, sep='\n'):
    return _rst(('```\n', '\n```'), *content, sep)


def link(title, url):
    return "[title](url)".format(title=title, url=url)


def escape_md(*content, sep=' '):
    result = text(*content, sep)
    for symbol in MARKDOWN_SYMBOLS + '[':
        result = result.replace(symbol, '\\' + symbol)
    return result