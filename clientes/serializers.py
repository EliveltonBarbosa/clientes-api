from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError('Não inclua números neste campo.')
        return nome
    
    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError('O CPF deve ter exatamente 11 dígitos.')
        return cpf
    