from rest_framework import serializers
from .models import Z2HPlanDetails

class Z2HPlanDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Z2HPlanDetails
        fields = (
            'id', 'is_active', 'uid', 'name', 'level_one_amount', 'level_two_amount', 'level_three_amount', 'level_four_amount',
        )