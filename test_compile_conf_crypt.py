import unittest
from compile_conf_rsa import CRSA

class TestCompileConfCrypt(unittest.TestCase):

    def setUp(self):
        self.rsa_public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxnH0e9B8oCqzVjxnRMd4
k2zASVSKyP0LebzssmiGkegBWlnUCwFa8/nxRtmsRwqkpgt23avRq4KdQHp+9zGY
w35lrK8L6+S9KU/fu7B9t9usC7jHiIyaTN7FNaBnRVO3DSJ0XjMvNr7hu+nruCqF
81FzlNDw+zBdp/eq8RdlJRqtWcb4CPLs9mxd0VUfcSk9/YGWuShOCSNHMCMXhmHn
5k6JV5MeSgktenZNzKg0TGD89wd0BaBfjWISnXGcCNpQCLL1HLw9LokoLoxsOSWE
q/3EaJ4LLrVCWYv9he3uCNpqPuWARJkSKgUkoNA56zRy1cBut67n6kMTpHHktGmR
rQIDAQAB
-----END PUBLIC KEY-----
"""
        self.rsa_private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAxnH0e9B8oCqzVjxnRMd4k2zASVSKyP0LebzssmiGkegBWlnU
CwFa8/nxRtmsRwqkpgt23avRq4KdQHp+9zGYw35lrK8L6+S9KU/fu7B9t9usC7jH
iIyaTN7FNaBnRVO3DSJ0XjMvNr7hu+nruCqF81FzlNDw+zBdp/eq8RdlJRqtWcb4
CPLs9mxd0VUfcSk9/YGWuShOCSNHMCMXhmHn5k6JV5MeSgktenZNzKg0TGD89wd0
BaBfjWISnXGcCNpQCLL1HLw9LokoLoxsOSWEq/3EaJ4LLrVCWYv9he3uCNpqPuWA
RJkSKgUkoNA56zRy1cBut67n6kMTpHHktGmRrQIDAQABAoIBAAmuM2v6zqmNi7QQ
PEVpqaMfcf3hxudpGK82nSFS4gWqGK7MpQBob4RpU/DN246XoVKMSp8jq5W/SGaF
0z3ByJ74woL7Awzd2rByOgrQ4EEg0TK9L9akbT6Eu4ATNBZ4r/xPCvgxbQMxqpdd
IOeaA3DML2Q6ERdf06HG/irGpmN55Ku3RNkMc7xOeh/wgZM8XkQpmB5mGcrS0sPe
bi42rn51QbCWIgiQeRIPn/dmkTFRwy8r3LT35wfgjPt+eUc0zCTFHGoqixSIgHII
sl5rK/dtVKmm+dypBaE4B6EpM/sCKe7L17vZcLjiqejcXrUOBA8hedBinWvpRQJw
ErcqqW0CgYEA2V066ejnFAtjyDrDk1anzLszenMin4bKcV9ZCyg++EU9aeNa0Y7z
4xGtzOnRjAK0eWCzLdeCHNuLgl1PK2hUTxRYWumsI8PWnHCLIGJmnCytrm0u0WuS
e3Jxtf9vC5X+MU6rRFXCewmEKewZlye1q2S1QB90fBDUSWj6OyfyxzMCgYEA6bfY
9lFEt8lODhFaahegoalz9qOIRNDucsmRHGlHJ0UpIjBpGIvMXxsigXHPUrJV6Zuw
xUXaCWDqbu+K4Eb+VBtpAEXiRtAvn/VTV0fEuQuAH6wwZ9WkebDrSZeQpmAccoP7
5K0Aqf+kY4/vw4939qyTomTyIQRgs/6vD92Mw58CgYAUncsgtH52YD4ul6RFLUrt
GDRhwNnf16EL78c6T67pTWftyyqqBa0MNHkPnn3JkdgcSxezmWU153zr+H2x2Etm
1L8soE07dy+71tDbWXnyBirTCHgQVOun2cr/QCMALlHVy2hjKt8vXE+0yjgDJjkM
8JhgZJtfyRjZfaN+SOO2EQKBgQCupciGQDJ2mAIw9vy2XNOXGnZibs9shSg6NK+w
KGeYS9EyEDTot8bPpwpA6pf/du5GNCaDM/B7o6VroqsHb2Wr2hO7tX0iZ32/LWbK
yQGTOanTgStm3DodCXy5MH5SJW38kO4RcsoVPshL8go7+6Csf0ePSZm53Hia6I1O
8MK4hwKBgGHkgtReT82Nsps0Opa6ImQFRWNh5iF1FCwwBi0DLvcvbNamUCC06it3
IloA7ilRyIkDvR0bg28peCG6XVfM04kDIXZQmQijr00LxrwwoYpw893jzgbi3hUy
WKzRIBni4/TkkAAHrVXUqd+qQ65i9S5EfRv6mHkcw5Om93T7g/RE
-----END RSA PRIVATE KEY-----
"""

    def test_encrypt(self):
        self.assertEqual(CRSA.encrypt(self.rsa_public_key, b'zasifrovany text'), [b"@\xe1\x1f\x1d\xc1m\xa8\x1ay7\x0b\xa88\x91\x8c\xb9\xfb\xec.\r\x8f\xe3\x7fV\x86\xd9z\x99A\xa71@}\xab~\xe9\xa7\xd9\xd5]\xc7'\x8b\xb0\x1bu\xb5\xe5N\x8f\xccd|\xd7\xc8\xba\x8a~U\xa8\xce!\xcd\xb8g\x0b\xb1!b\xc8\xec\xd9wR\xbf\xcdY\xb3`\xcc\xbf\xf0}\x85~0\xd1|\xe8\xf0\x86\xa8`j$\x99`:\xa7\x00~\xea\xc0\x85\x92G\xdc\xee\x0f\xe1\xa7Z\xfe]\xd1$\xa8{\xa0\xccW=\xb0\xf7\x99\x1alR\x82\xe2\xba\x85\xf6\xb8\xd0\x00\x88Zrh\xc0\xd4\xe8gI\x06B\x84AFf\xb4\xa7]b\x08\x82I\x8d [\xa1Z;\x1a\xa5\xb5\xbe\x98\x8d\xd7\x15\xaa\xf5\xeb#\x05R`y\x8f\xfd\x0f\xb7[\x06\x87\x10\xad~_\x99\x14|\xfb\xa0\x13\xafD\x92\xd5\xb1\x95\xd0\xdcZY\x0b\x04\x08\xc5\xa6\x9e\x96f\x95\xe5\x8a5\xf5\xe5ri\xc5fP\x80\xbe\x1c\x02\x14NR\xa8\x995Zd\xee\xf8\x9b\xdb<\x14\xd3\xc1\xfbt\xdb\x96\xec4\xf9\xe2_\xf6"])

    def test_bytes_to_int(self):
        self.assertEqual(CRSA.bytes_to_int(b'aha'), 6383713)

    def test_int_to_bytes(self):
        self.assertEqual(CRSA.int_to_bytes(6383713, 5), b'\x00\x00aha')

    def test_encrypt_by_pow(self):
        public_key = CRSA.import_key(self.rsa_public_key)
        self.assertEqual(CRSA.encrypt_by_pow(public_key, b'zasifrovany text', 2000), b"@\xe1\x1f\x1d\xc1m\xa8\x1ay7\x0b\xa88\x91\x8c\xb9\xfb\xec.\r\x8f\xe3\x7fV\x86\xd9z\x99A\xa71@}\xab~\xe9\xa7\xd9\xd5]\xc7'\x8b\xb0\x1bu\xb5\xe5N\x8f\xccd|\xd7\xc8\xba\x8a~U\xa8\xce!\xcd\xb8g\x0b\xb1!b\xc8\xec\xd9wR\xbf\xcdY\xb3`\xcc\xbf\xf0}\x85~0\xd1|\xe8\xf0\x86\xa8`j$\x99`:\xa7\x00~\xea\xc0\x85\x92G\xdc\xee\x0f\xe1\xa7Z\xfe]\xd1$\xa8{\xa0\xccW=\xb0\xf7\x99\x1alR\x82\xe2\xba\x85\xf6\xb8\xd0\x00\x88Zrh\xc0\xd4\xe8gI\x06B\x84AFf\xb4\xa7]b\x08\x82I\x8d [\xa1Z;\x1a\xa5\xb5\xbe\x98\x8d\xd7\x15\xaa\xf5\xeb#\x05R`y\x8f\xfd\x0f\xb7[\x06\x87\x10\xad~_\x99\x14|\xfb\xa0\x13\xafD\x92\xd5\xb1\x95\xd0\xdcZY\x0b\x04\x08\xc5\xa6\x9e\x96f\x95\xe5\x8a5\xf5\xe5ri\xc5fP\x80\xbe\x1c\x02\x14NR\xa8\x995Zd\xee\xf8\x9b\xdb<\x14\xd3\xc1\xfbt\xdb\x96\xec4\xf9\xe2_\xf6")

    def test_format_value(self):
        encrypted_bytes = CRSA.encrypt(self.rsa_public_key, b'zasifrovany text')
        self.assertEqual(CRSA.format_value(encrypted_bytes), '{~$QOEfHcFtqBp5NwuoOJGMufvsLg2P439Whtl6mUGnMUB9q37pp9nVXccni7AbdbXlTo/MZHzXyLqKflWoziHNuGcLsSFiyOzZd1K/zVmzYMy/8H2FfjDRfOjwhqhgaiSZYDqnAH7qwIWSR9zuD+GnWv5d0SSoe6DMVz2w95kabFKC4rqF9rjQAIhacmjA1OhnSQZChEFGZrSnXWIIgkmNIFuhWjsapbW+mI3XFar16yMFUmB5j/0Pt1sGhxCtfl+ZFHz7oBOvRJLVsZXQ3FpZCwQIxaaelmaV5Yo19eVyacVmUIC+HAIUTlKomTVaZO74m9s8FNPB+3Tbluw0+eJf9g==}\n')

    def test_decrypt(self):
        self.assertEqual(CRSA.decrypt(self.rsa_private_key, b"@\xe1\x1f\x1d\xc1m\xa8\x1ay7\x0b\xa88\x91\x8c\xb9\xfb\xec.\r\x8f\xe3\x7fV\x86\xd9z\x99A\xa71@}\xab~\xe9\xa7\xd9\xd5]\xc7'\x8b\xb0\x1bu\xb5\xe5N\x8f\xccd|\xd7\xc8\xba\x8a~U\xa8\xce!\xcd\xb8g\x0b\xb1!b\xc8\xec\xd9wR\xbf\xcdY\xb3`\xcc\xbf\xf0}\x85~0\xd1|\xe8\xf0\x86\xa8`j$\x99`:\xa7\x00~\xea\xc0\x85\x92G\xdc\xee\x0f\xe1\xa7Z\xfe]\xd1$\xa8{\xa0\xccW=\xb0\xf7\x99\x1alR\x82\xe2\xba\x85\xf6\xb8\xd0\x00\x88Zrh\xc0\xd4\xe8gI\x06B\x84AFf\xb4\xa7]b\x08\x82I\x8d [\xa1Z;\x1a\xa5\xb5\xbe\x98\x8d\xd7\x15\xaa\xf5\xeb#\x05R`y\x8f\xfd\x0f\xb7[\x06\x87\x10\xad~_\x99\x14|\xfb\xa0\x13\xafD\x92\xd5\xb1\x95\xd0\xdcZY\x0b\x04\x08\xc5\xa6\x9e\x96f\x95\xe5\x8a5\xf5\xe5ri\xc5fP\x80\xbe\x1c\x02\x14NR\xa8\x995Zd\xee\xf8\x9b\xdb<\x14\xd3\xc1\xfbt\xdb\x96\xec4\xf9\xe2_\xf6"), b'zasifrovany text')

if __name__ == '__main__':
    unittest.main()
