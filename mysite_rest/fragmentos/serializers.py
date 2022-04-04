from django.contrib.auth.models import User

from rest_framework import serializers

from fragmentos.models import Fragmento, LENGUAGE_CHOICES, STYLE_CHOICES


#	-- Heredando de serializers.HyperlinkedModelSerializer --
class SerializadorFragmento(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name = 'fragmentos_detalles_highlight',
                                                     format='html')
    url = serializers.HyperlinkedIdentityField(
        view_name = 'fragmentos_detalles',
    )

    class Meta:
        model = Fragmento
        fields = ['url', 'id', 'created', 'owner', 'title', 'code', 'highlight', 'linenos', 'lenguage', 'style']

class SerializadorUser(serializers.HyperlinkedModelSerializer):
    #zona de pruebas
#    lookup_field = ''
    fragmentos = serializers.HyperlinkedRelatedField(many = True,
                                                     read_only = True,
                                                     view_name = 'fragmentos_detalles',)

    url = serializers.HyperlinkedIdentityField(
        view_name = 'usuarios_detalles',
    )
    #fin zona de pruebas

#    fragmentos = serializers.HyperlinkedRelatedField(many = True, view_name = 'fragmentos_lista', read_only = True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'fragmentos']

# ------------------------------------------------------------------------------
'''
#	-- Heredando de serializers.ModelSerializer --
class SerializadorFragmento(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')

    class Meta:
        model = Fragmento
        fields = ['id', 'created', 'owner', 'title', 'code', 'linenos', 'lenguage', 'style']


class SerializadorUser(serializers.ModelSerializer):
    fragmentos = serializers.PrimaryKeyRelatedField(many = True, queryset = Fragmento.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'fragmentos']

# -------------------------------------------------------------------------------

#	-- Heredando de Serializer --
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
