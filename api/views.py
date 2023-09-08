from .serializers import CustomerSerializer,ProductSerializer,CartSerializer,OrderSerializer
from rest_framework.views import APIView
from customer.models import Customer
from inventory.models import Product
from rest_framework.response import Response
from rest_framework import status
from cart.models import Cart
from order.models import Order


class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer= CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CustomerDetailView(APIView):
    def get(self,request,id,format=None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    def put(self,request,id,format=None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id,format=None):
        customer = Customer.objects.get(id=id)
        customer.delete()
        return Response("customer deleted", status=status.HTTP_204_NO_CONTENT)
    
    
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer= ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
    
    
class ProductDetailView(APIView):
    def get(self,request,id,format=None):
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    def put(self,request,id,format=None):
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id,format=None):
        product = Product.objects.get(id=id)
        product.delete()
        return Response("product deleted", status=status.HTTP_204_NO_CONTENT)
        
    
class CartListView(APIView):
    def get(self, request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer= CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    
class CartDetailView(APIView):
    def get(self,request,id,format=None):
        cart = Cart.objects.get(id=id)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    def put(self,request,id,format=None):
        cart = Cart.objects.get(id=id)
        serializer = CartSerializer(cart,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id,format=None):
        cart = Cart.objects.get(id=id)
        cart.delete()
        return Response("cart deleted", status=status.HTTP_204_NO_CONTENT)
            
    
class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer= OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class OrderDetailView(APIView):
    def get(self,request,id,format=None):
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    def put(self,request,id,format=None):
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id,format=None):
        order = Order.objects.get(id=id)
        order.delete()
        return Response("cart deleted", status=status.HTTP_204_NO_CONTENT)    
              
          
    
    
  
