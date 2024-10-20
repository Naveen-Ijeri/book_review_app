

def encrypt_password(password, hash_name="sha1", salt=b'MnkSaltEncKey', iterations=10000, dklen=64):
    from hashlib import pbkdf2_hmac
    import base64
    key = pbkdf2_hmac(
        hash_name=hash_name,
        password=password.encode(),
        salt=salt,
        iterations=iterations,
        dklen=dklen
    )
    return base64.b64encode(key).decode('utf-8')


class ErrorResponse(object):
    AUTHENTICATION_ERROR = 'authentication error'

    @staticmethod
    def get_response_obj(error_type, message, status=None):
        if status:
            return {
                "type": error_type,
                "message": message,
                "status": status
            }
        else:
            return {
                "type": error_type,
                "message": message
            }