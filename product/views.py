from .serializers import CategoryListSerializer, ProductListSerializer, ReviewListSerializer, CategoryDetailSerializer,ProductDetailSerializer, ReviewDetailSerializer, CategoryValidateSerializer, ProductValidateSerializer, ReviewValidateSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from django.db import transaction
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategoryListSerializer
        return CategoryValidateSerializer

class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategoryDetailSerializer
        return CategoryValidateSerializer

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.prefetch_related('reviews').all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductListSerializer
        return ProductValidateSerializer

class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.prefetch_related('reviews').all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductDetailSerializer
        return ProductValidateSerializer

class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewListSerializer
        return ReviewValidateSerializer

class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewDetailSerializer
        return ReviewValidateSerializer


# @api_view(http_method_names=['GET', 'POST'])
# def category_list_create_api_view(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         data = CategoryListSerializer(categories, many=True).data
#
#         return Response(
#             data=data,
#             status=status.HTTP_200_OK
#         )
#     elif request.method == "POST":
#         serializer = CategoryValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data=serializer.errors)
#         name = serializer.validated_data.get('name')
#
#         with transaction.atomic():
#             category = Category.objects.create(
#                 name=name,
#             )
#             return Response(status=status.HTTP_201_CREATED,
#                             data=CategoryDetailSerializer(category).data)
#
# @api_view(http_method_names=['GET', 'PUT', 'DELETE'])
# def category_detail_api_view(request, id):
#     try:
#         category = Category.objects.get(id=id)
#     except Category.DoesNotExist:
#         return Response(data={'error': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         data = CategoryDetailSerializer(category, many=False).data
#
#         return Response(
#             data=data,
#             status=status.HTTP_200_OK
#         )
#     elif request.method == 'PUT':
#         serializer = CategoryValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data=serializer.errors)
#         category.name = serializer.validated_data.get('name')
#         category.save()
#         return Response(
#             status=status.HTTP_201_CREATED,
#             data=CategoryDetailSerializer(category).data
#         )
#     elif request.method == 'DELETE':
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(http_method_names=['GET', 'POST'])
# def product_list_create_api_view(request):
#     if request.method == 'GET':
#         products = Product.objects.prefetch_related('reviews')
#         data = ProductListSerializer(products, many=True).data
#
#         return Response(
#             data=data,
#             status=status.HTTP_200_OK
#         )
#     elif request.method == 'POST':
#         serializer = ProductValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data=serializer.errors)
#         title = serializer.validated_data.get('title')
#         description = serializer.validated_data.get('description')
#         category_id = serializer.validated_data.get('category_id')
#
#         with transaction.atomic():
#             product = Product.objects.create(
#                 title=title,
#                 description=description,
#                 category_id=category_id,
#             )
#             product.save()
#
#             return Response(status=status.HTTP_201_CREATED,
#                             data=ProductDetailSerializer(product).data)
#
#
#
# @api_view(http_method_names=['GET', 'PUT', 'DELETE'])
# def product_detail_api_view(request, id):
#     try:
#         product = Product.objects.get(id=id)
#     except Product.DoesNotExist:
#         return Response(data={'error': 'product not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         data = ProductDetailSerializer(product, many=False).data
#
#         return Response(
#             data=data,
#             status=status.HTTP_200_OK
#         )
#     elif request.method == 'PUT':
#         serializer = ProductValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data=serializer.errors)
#         product.title = serializer.validated_data.get('title')
#         product.description = serializer.validated_data.get('description')
#         product.category_id = serializer.validated_data.get('category_id')
#         product.save()
#         return Response(
#             status=status.HTTP_201_CREATED,
#             data=ProductDetailSerializer(product).data
#         )
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
#
# @api_view(http_method_names=['GET', 'POST'])
# def review_list_create_api_view(request):
#     if request.method == 'GET':
#
#         reviews = Review.objects.all()
#         data = ReviewListSerializer(reviews, many=True).data
#
#         return Response(
#             data=data,
#             status=status.HTTP_200_OK
#         )
#     elif request.method == 'POST':
#         serializer = ReviewValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data=serializer.errors)
#         stars = serializer.validated_data.get('stars')
#         text = serializer.validated_data.get('text')
#         product_id = serializer.validated_data.get('product_id')
#
#         review = Review.objects.create(
#             stars=stars,
#             text=text,
#             product_id=product_id,
#         )
#         return Response(status=status.HTTP_201_CREATED,
#                         data=ReviewDetailSerializer(review).data)
#
# @api_view(http_method_names=['GET','PUT','DELETE'])
# def review_detail_api_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(data={'error': 'review not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         data = ReviewDetailSerializer(review, many=False).data
#
#         return Response(
#             data=data,
#             status=status.HTTP_200_OK
#         )
#     elif request.method == 'PUT':
#          serializer = ReviewValidateSerializer(data=request.data)
#          if not serializer.is_valid():
#              return Response(status=status.HTTP_400_BAD_REQUEST,
#                              data=serializer.errors)
#          review.stars = serializer.validated_data.get('stars')
#          review.text = serializer.validated_data.get('text')
#          review.product_id = serializer.validated_data.get('product_id')
#          review.save()
#          return Response(
#              status=status.HTTP_201_CREATED,
#              data=ReviewDetailSerializer(review).data
#          )
#
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)