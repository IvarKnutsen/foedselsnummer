from django.test import TestCase, Client

class PersonalIDViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_returns_200(self):
        response = self.client.get("/personalID/")
        self.assertEqual(response.status_code, 200)

    def test_index_contains_11_digit_id(self):
        response = self.client.get("/personalID/")
        content = response.content.decode()
        # Extract the last word, which should be the generated ID
        fnr = content.strip().split()[-1]
        self.assertEqual(len(fnr), 11)
        self.assertTrue(fnr.isdigit())
