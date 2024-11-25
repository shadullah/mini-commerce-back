from django.shortcuts import render

from .serializers import CartSerializer, CartItemSerializer
from .models import Cart,CartItem

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.

# all user cart fetching api
class CartListView(ListAPIView):
    queryset = Cart.objects.prefetch_related('cart_items').all()
    serializer_class = CartSerializer

# specific user cart get , post
class CartByUserView(APIView):
    def get(self, req, user_id):
        try:
            cart = Cart.objects.all().get(customer__id=user_id)
            
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
                
        except:
            return Response({"error":"No cart found"}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, req, user_id):
        try:
            cart = Cart.objects.get(customer_id=user_id)
            data = req.data
            data['cart']=cart.id

            # filter existing item
            existing_item = CartItem.objects.filter(cart=cart, title=data.get('title'))
            if existing_item:
                return Response(
                    {"error": "An item with the same name already exists in the cart."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            serializer = CartItemSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Cart.DoesNotExist:
            return Response({"error":"Cart not found"}, status=status.HTTP_404_NOT_FOUND)
        
# cart delete , update
class CartItemUpdateDelete(APIView):
    def get(self, req, user_id,cartItem_id):
        try:
            cart = Cart.objects.all().get(customer__id=user_id)
            cart_item = CartItem.objects.get(id=cartItem_id, cart=cart)
            
            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
                
        except:
            return Response({"error":"No cart found"}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, user_id, cartItem_id):
        try:
            cart = Cart.objects.get(customer_id=user_id)
            cart_item = CartItem.objects.get(id=cartItem_id, cart=cart)
            serializer = CartItemSerializer(cart_item, data= request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Cart.DoesNotExist:
            return Response({"error":"Cart not found"}, status=status.HTTP_404_NOT_FOUND)
        except CartItem.DoesNotExist:
            return Response({"error":"CartItem not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, user_id, cartItem_id):
        try:
            cart = Cart.objects.get(customer_id=user_id)
            cart_item = CartItem.objects.get(id=cartItem_id, cart=cart)
            cart_item.delete()
            return Response( status=status.HTTP_204_NO_CONTENT)
        except Cart.DoesNotExist:
            return Response({"error":"Cart not found"}, status=status.HTTP_404_NOT_FOUND)
        except CartItem.DoesNotExist:
            return Response({"error":"CartItem not found"}, status=status.HTTP_404_NOT_FOUND)



