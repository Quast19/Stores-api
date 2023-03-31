from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import IdOffset
class IdOffsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdOffset
        fields=[
            # 'email',
            #'name', 
            'store_id',
            'loc',
            'name',
            'abbrevation',
            'offset',
            'is_dst',
        ]
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(
    #             f"{value} is already a product name."
    #         )
    #     return value
    #validator later implemented in validatros .py 
    
    

    
    
    # to create and update in a serializer bruh
    # def create(self, validated_data):
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     print(email, obj)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email'
    #     )
        
    #     instance.title = validated_data.get('title')
    #     return  super.update(instance, validated_data)
    
    
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk":obj.pk}, request = request)
    def get_my_discount(self, obj):
        if not hasattr(obj , 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()