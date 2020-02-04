from django.test import TestCase

from order.models import Order


class TestOrder(TestCase):

    def test_orders_string_repr(self):
        order = Order.objecs.create(
            chat_id='199945',
            first_name='Max',
            last_name='Max',
            company_name='Greatsoft',
            phone_number='+998935789768',
            comment='this is the comment'
        )

        self.assertTrue(str(order), '+998935789768')
