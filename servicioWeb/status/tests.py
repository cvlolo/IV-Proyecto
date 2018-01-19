from django.test import TestCase
from django.core.urlresolvers import reverse

class DjangoTestCase(TestCase):
    def test_status(self):
        response = self.client.get(reverse('root'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "status")
	

