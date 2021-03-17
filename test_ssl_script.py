import unittest
import ssl_script
import datetime


class TestSSLScript(unittest.TestCase):
    def test_ssl_information(self):
        result = ssl_script.ssl_information("google.com")
        print(result)

        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("It is", current_time, "and I'm still running tests..")

        data = {
            'subject': '*.google.com',
            'issuer': 'GTS CA 1O1',
            'start': 'Feb 23 15:36:56 2021 GMT',
            'end': 'May 18 15:36:55 2021 GMT'
        }

        self.assertEqual(result["subject"], data["subject"])
        self.assertEqual(result["issuer"], data["issuer"])
        self.assertEqual(result["start"], data["start"])
        self.assertEqual(result["end"], data["end"])


if __name__ == '__main__':
    unittest.main()
