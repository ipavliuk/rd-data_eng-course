from unittest import TestCase, mock

from lec02.job2 import main

class MainFunctionTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        main.app.testing = True
        cls.client = main.app.test_client()

    def test_return_400_stg_dir_param_missed(self) -> None:
        """
        Raise 400 HTTP code when no 'stg_dir' param
        """
        resp = self.client.post('/', json={'raw_dir': '/foo/bar/'})
        self.assertEqual(400, resp.status_code)

    def test_return_400_raw_dir_param_missed(self) -> None:
        """
        Raise 400 HTTP code when no 'raw_dir' param
        """
        resp = self.client.post('/', json={'stg_dir': '/foo/bar'})

        self.assertEqual(400, resp.status_code)


    @mock.patch("lec02.job2.main.migrate_to_avro")
    def test_migrate_to_avro_called_with_correct_params(
            self, migrate_mock: mock.MagicMock
    ) -> None:

        fake_stg_dir = "/tmp/stg"
        fake_raw_dir = "/tmp/raw"

        self.client.post("/", json={"stg_dir": fake_stg_dir, "raw_dir": fake_raw_dir})

        migrate_mock.assert_called_once_with(fake_raw_dir, fake_stg_dir)

    @mock.patch("lec02.job2.main.migrate_to_avro")
    def test_return_201_when_all_is_ok(
            self, migrate_mock: mock.MagicMock
    ) -> None:
        resp = self.client.post(
            "/",
            json={
                "stg_dir": "D:\\test_data\\stg\\sales\\2022-08-09",
                "raw_dir": "D:\\test_data\\raw\\sales\\2022-08-09",
            },
        )

        self.assertEqual(201, resp.status_code)
        print(resp.get_json())