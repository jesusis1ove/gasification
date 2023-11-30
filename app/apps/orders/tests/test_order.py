import datetime

from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from mixer.backend.django import mixer

from ..views import OrderViewSet
from ..models import Order

from ...erp_data.models import Counterparty


class OrderAsUserTest(APITestCase):

    def setUp(self):
        self.user = mixer.blend(get_user_model(), is_staff=False)
        self.counterparty = mixer.blend(Counterparty, counterparty_inn=self.user.login, guid=mixer.RANDOM)
        self.order = mixer.blend(Order, created_by=self.user)

        self.client.force_authenticate(user=self.user)

    def test_get_authenticated_user(self):
        url = reverse('orders-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_unauthenticated_user(self):
        self.client.logout()
        url = reverse('orders-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create(self):
        url = reverse('orders-list')
        data = {
            'construction_object_guid': 'objectguid',
            'applicant': 'applicant',
            'date': datetime.date.today(),
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        created_order = Order.objects.all().order_by('-id').first()
        self.assertEquals(created_order.status, 'created')

    def test_accept(self):
        url = reverse('orders-detail', args=[self.order.id])
        url = f'{url}accept/'
        response = self.client.put(url)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cancel(self):
        url = reverse('orders-detail', args=[self.order.id])
        url = f'{url}cancel/'
        response = self.client.put(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)



