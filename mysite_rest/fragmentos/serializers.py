from rest_framework import serializers

from fragmentos.models import Fragmento, LENGUAGE_CHOICES, STYLE_CHOICES

'''# Heredando de Serializer
class SerializadorFragmento(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    created = serializers.DateTimeField()
    title = serializers.CharField(required = False, allow_blank = True, max_length = 100)
    code = serializers.CharField(style = {'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required = False)
    lenguage = serializers.ChoiceField(choices = LENGUAGE_CHOICES, default = 'python')
    style = serializers.ChoiceField(choices = STYLE_CHOICES, default = 'friendly')

    def create(self, validated_data):
        # crea y devuelve una nueva instancia de 'Fragmento', recibiendo los datos en validated_data
        return Fragmento.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # actualiza y devuelve una instancia de 'Fragmento', recibiendo los datos en validated_data
        instance.title = validate_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.lenguage = validated_data.get('lenguage', instance.lenguage)
        instance.style = validated_data.get('style', instance.style)

        instance.save()

        return instance
'''
class SerializadorFragmento(serializers.ModelSerializer):
    class Meta:
        model = Fragmento
        fields = ['id', 'created', 'title', 'code', 'linenos', 'lenguage', 'style']
