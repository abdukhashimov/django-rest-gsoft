import re
from rest_framework import serializers

from .models import BaseContact, Order


class BaseContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseContact
        fields = ('phone_number', )

    def validate(self, attrs):
        number = attrs.get('phone_number')
        cond = re.match(
            '(\+\d{3}[ \-]?)?\d{2}[ \-]?\d{3}[ \-]?\d{2}[ \-]?\d{2}', number)
        if not cond:
            raise serializers.ValidationError('Phone number is not correct')
        return attrs


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('phone_number', 'first_name',
                  'last_name', 'company_name', 'comment')

    def validate(self, attrs):
        number = attrs.get('phone_number')
        cond = re.match(
            '(\+\d{3}[ \-]?)?\d{2}[ \-]?\d{3}[ \-]?\d{2}[ \-]?\d{2}', number)
        if not cond:
            raise serializers.ValidationError('Phone number is not correct')
        return attrs
