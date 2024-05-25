from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import cpf_valido, nome_valido, rg_valido, celular_valido 

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': 'Não inclua números neste campo.'})
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'O CPF deve ter 11 dígitos.'})
        if not rg_valido(data['rg']): 
            raise serializers.ValidationError({'rg': 'O RG deve ter exatamente 9 dígitos.'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': 'O número de celular deve seguir o seguinte formato: 11 91234-11234 (Contendo código de área e respeitando espaços e hífen).'})
        return data
    