import unittest

from Task2.app import create_app

app = create_app()


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_predict_gdp(self):
        input_data = {
            "2019": "300",
            "2011": "567",
            "2017": "748",
            "2015": "78",
            "2018": "89"
        }
        response = self.client.post(
            '/predict_gdp',
            json=input_data)
        data = response.get_json()
        self.assertEqual(
            response.status_code,
            200)
        self.assertNotEqual(
            data.get("predicted_GDP_per_capita"), None)


if __name__ == '__main__':
    unittest.main()
