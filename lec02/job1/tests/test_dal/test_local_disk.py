"""
Tests dal.local_disk.py module
# TODO: write tests
"""
from unittest import TestCase, mock
import tempfile
import json
import os
from lec02.job1.dal.local_disk import save_to_disk
from lec02.job1.tests.test_dal.test_sales_api import SAMPLE_SALES_DATA


class SaveToDiskTestCase(TestCase):
    """
    Test dal.local_disk.save_to_disk function.
    # TODO: implement
    """
    def test_writes_file_with_exact_content(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "sales_2022‑08‑09.json")

            # Act
            save_to_disk(SAMPLE_SALES_DATA, path)

            # Assert
            self.assertTrue(os.path.isfile(path))
            with open(path, encoding="utf-8") as fp:
                loaded = json.load(fp)

            self.assertEqual(SAMPLE_SALES_DATA, loaded)
