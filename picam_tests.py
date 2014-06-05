import os
import picam
import unittest
import tempfile


class PicamTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, picam.app.config['DATABASE'] = tempfile.mkstemp()
        picam.app.config['TESTING'] = True
        self.app = picam.app.test_client()
        picam.db.create_all()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(picam.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        assert rv.data

if __name__ == '__main__':
    unittest.main()
