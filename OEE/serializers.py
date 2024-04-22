from.models import machines
from.models import product_log
from rest_framework import serializers
from.models import oee

class machine0(serializers.ModelSerializer):
    class Meta:
        model=machines
        fields='__all__'

class product_log0(serializers.ModelSerializer):
    class Meta:
        model = product_log
        fields = '__all__'

class oee_information(serializers.ModelSerializer):
    class Meta:
        model = oee
        fields = '__all__'