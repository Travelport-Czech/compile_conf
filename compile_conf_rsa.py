import math
from Crypto.PublicKey import RSA
from Crypto import Random
import base64

class CRSA:
    @staticmethod
    def create_key(filename):
        # RSA modulus length must be a multiple of 256 and >= 1024
        modulus_length = 1024 * 2
        privatekey = RSA.generate(modulus_length, Random.new().read)
        publickey = privatekey.publickey()
        open(filename, 'w').write(publickey.exportKey())
        open(filename + '.priv', 'w').write(privatekey.exportKey())
        return publickey.exportKey()

    @staticmethod
    def bytes_to_int(bytes_value):
        if hasattr(int, 'from_bytes'):
            return int.from_bytes(bytes_value, 'big')
        result = 0
        for b in bytes_value:
            result = result * 256 + ord(b)
        return result

    @staticmethod
    def int_to_bytes(value, length):
        if hasattr(int, 'to_bytes'):
            return value.to_bytes(length, 'big')
        result = (chr(value >> (i * 8) & 0xff) for i in range(length - 1, -1, -1))
        return b''.join(result)

    @staticmethod
    def encrypt_by_pow(publickey, data, length):
        if len(data) > length:
            raise ValueError()
        ct_int = CRSA.bytes_to_int(data)
        pt_int = pow(ct_int, publickey.e, publickey.n)
        encrypted_msg = CRSA.int_to_bytes(
            pt_int, length).lstrip(b'\x00')
        return encrypted_msg

    @staticmethod
    def import_key(key_value):
        return RSA.importKey(key_value)

    @staticmethod
    def encrypt(key_value, data):
        def try_encrypt(publickey, data):
            try:
                encrypted_msg = publickey.encrypt(data, 32)[0]
            except NotImplementedError:
                encrypted_msg = CRSA.encrypt_by_pow(publickey, data, publickey.size_in_bytes())
            return encrypted_msg

        def try_chunk(publickey, data, divider):
            chunk_len = int(math.ceil(float(len(data)) / divider))
            chunks = []
            while data:
                chunks.append(try_encrypt(publickey, data[:chunk_len]))
                data = data[chunk_len:]
            return chunks

        publickey = CRSA.import_key(key_value)
        for divider in range(1, 21):
            try:
                return try_chunk(publickey, data, divider)
            except ValueError:
                pass
        return try_chunk(publickey, data, 1)

    @staticmethod
    def format_value(encrypted):
        return ''.join('{~$%s}\n' % base64.standard_b64encode(chunk).decode('ascii')
                       for chunk in encrypted)

    @staticmethod
    def decrypt_by_pow(key, data, length):
        ct_int = CRSA.bytes_to_int(data)
        pt_int = pow(ct_int, key.d, key.n)
        decrypted_msg = CRSA.int_to_bytes(
            pt_int, length).lstrip(b'\x00')
        return decrypted_msg

    @staticmethod
    def decrypt(key_value, data):
        key = RSA.importKey(key_value)
        try:
            decrypted_message = key.decrypt(data)
        except NotImplementedError:
            decrypted_message = CRSA.decrypt_by_pow(key, data, key.size_in_bytes())
        return decrypted_message
