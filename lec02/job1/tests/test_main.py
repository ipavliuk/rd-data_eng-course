"""
Tests for main.py
# TODO: write tests
"""
from unittest import TestCase, mock

# NB: avoid relative imports when you will write your code
#from .. import main
import main


class MainFunctionTestCase(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        main.app.testing = True
        cls.client = main.app.test_client()


    @mock.patch('lec02.job1.main.save_sales_to_local_disk')
    def test_return_400_date_param_missed(
            self,
            get_sales_mock: mock.MagicMock
        ):
        """
        Raise 400 HTTP code when no 'date' param
        """
        resp = self.client.post(
            '/',
            json={
                'raw_dir': '/foo/bar/',
                # no 'date' set!
            },
        )

        self.assertEqual(400, resp.status_code)

    def test_return_400_raw_dir_param_missed(self):
        """
        Raise 400 HTTP code when no 'raw_dir' param
        """
        resp = self.client.post(
            '/',
            json={
                'date': '2022-08-09',
                # no 'raw_dir' set!
            },
        )

        self.assertEqual(400, resp.status_code)

    @mock.patch('lec02.job1.main.save_sales_to_local_disk')
    def test_save_sales_to_local_disk(
            self,
            save_sales_to_local_disk_mock: mock.MagicMock
    ):
        """
        Test whether api.get_sales is called with proper params
        """
        fake_date = '1970-01-01'
        fake_raw_dir = '/foo/bar'
        self.client.post(
            '/',
            json={
                'date': fake_date,
                'raw_dir': fake_raw_dir,
            },
        )

        save_sales_to_local_disk_mock.assert_called_with(
            date=fake_date,
            raw_dir=fake_raw_dir,
        )

    @mock.patch('lec02.job1.main.save_sales_to_local_disk')
    def test_return_201_when_all_is_ok(
            self,
            get_sales_mock: mock.MagicMock
    ):
        date = '2022-08-09'
        raw_dir = 'D:\\test_data\\raw\\sales\\2022-08-09\\sales_2022-08-09.json'
        self.client.post(
            '/',
            json={
                'date': date,
                'raw_dir': raw_dir,
            },
        )

        get_sales_mock.assert_called_with(
            date=date,
            raw_dir=raw_dir,
        )
