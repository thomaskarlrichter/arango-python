
__all__ = ("RequestsBase",)


class RequestsBase(object):
    """
    Base class to implement HTTP client
    """
    @classmethod
    def build_response(cls, status, message, headers, body):
        d = {
            "text": body,
            "headers": headers,
            "message": message,
            "status_code": status}

        return type('ArangoHttpResponse', (object,), d)

    def get(*args, **kwargs):
        raise NotImplementedError

    def post(*args, **kwargs):
        raise NotImplementedError

    def put(*args, **kwargs):
        raise NotImplementedError

    def delete(*args, **kwargs):
        raise NotImplementedError
