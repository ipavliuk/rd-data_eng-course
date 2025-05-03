"""
Tests sales_api.py module.
# TODO: write tests
"""
from unittest import TestCase, mock

# NB: avoid relative imports when you will write your code:
from lec02.job1.dal.sales_api import get_sales

from lec02.job1.dal import sales_api

SAMPLE_SALES_DATA = [
    {"client": "Michael Wilkerson", "purchase_date": "2022-08-09",
     "product": "Vacuum cleaner", "price": 346},
    {"client": "Russell Hill", "purchase_date": "2022-08-09",
     "product": "Microwave oven", "price": 446},
    {"client": "Michael Galloway", "purchase_date": "2022-08-09",
     "product": "Phone", "price": 1042},
    {"client": "Tom Gonzalez", "purchase_date": "2022-08-09",
     "product": "TV", "price": 2438},
    {"client": "Ronald King", "purchase_date": "2022-08-09",
     "product": "coffee machine", "price": 1957},
]


class GetSalesTestCase(TestCase):
    """
    Test sales_api.get_sales function.
    # TODO: implement
    """

    @mock.patch("lec02.job1.dal.sales_api.requests.get")
    def test_calls_requests_get_and_returns_json(self, get_mock):
        # Arrange: mock HTTP response
        response_stub = mock.Mock()
        response_stub.json.return_value = SAMPLE_SALES_DATA
        get_mock.return_value = response_stub

        date = "2022-08-09"

        # Act
        result = sales_api.get_sales(date)

        # Assert: correct URL, auth header, and JSON payload
        expected_url = f"{sales_api.API_URL}sales?date={date}&page=1"
        get_mock.assert_called_once_with(
            expected_url,
            headers={"Authorization": sales_api.AUTH_TOKEN},
        )
        self.assertEqual(SAMPLE_SALES_DATA, result)
