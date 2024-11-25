from rest_framework.serializers import ModelSerializer, IntegerField, ValidationError

from .models import CartItem,Cart

class CartItemSerializer(ModelSerializer):
    customer_id = IntegerField(write_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "cart", "title", "quantity", "price", "image", "customer_id"]
        extra_kwargs = {"cart": {"read_only": True}}

    def create(self, validated_data):
        customer_id = validated_data.pop("customer_id")

        try:
            cart = Cart.objects.get(customer_id=customer_id)
        except Cart.DoesNotExist:
            raise ValidationError({"customer_id": "cart not found for this id"})
        
        return CartItem.objects.create(cart=cart, **validated_data)

class CartSerializer(ModelSerializer):
    cart_items = CartItemSerializer(many=True)

    class Meta: 
        model = Cart 
        fields = ["id", "customer", "created_at", "updated_at", "cart_items"]