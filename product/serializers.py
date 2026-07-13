from rest_framework import serializers
from .models import Category, Product, Review
from rest_framework.exceptions import ValidationError

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text'.split()


class CategoryListSerializer(serializers.ModelSerializer):
    products_count = serializers.ReadOnlyField()
    class Meta:
        model = Category
        fields = 'id name products_count'.split()


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class ProductListSerializer(serializers.ModelSerializer):
    reviews = ReviewListSerializer(many=True)
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = 'id title description reviews rating'.split()

    def get_rating(self, product):
        reviews_list = product.reviews.all()
        if not reviews_list:
            return 0.0
        total_stars = sum(i.stars for i in reviews_list if i.stars)
        return round(total_stars / len(reviews_list), 1)


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


# class CategoryValidateSerializer(serializers.Serializer):
#     name = serializers.CharField()

class CategoryValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

# class ProductValidateSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255, min_length=2)
#     description = serializers.CharField(required=False)
#     category_id = serializers.IntegerField()
#
#     def validate_category_id(self, category_id):
#         try:
#             Category.objects.get(id=category_id)
#         except Category.DoesNotExist:
#             raise ValidationError('Category not found!')
#         return category_id

class ProductValidateSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category'
    )

    class Meta:
        model = Product
        fields = ['title', 'description', 'category_id']

        extra_kwargs = {
            'title': {'min_length': 2, 'max_length': 255},
            'description': {'required': False, 'allow_blank': True}
        }


# class ReviewValidateSerializer(serializers.Serializer):
#     stars = serializers.IntegerField(min_value=1, max_value=5)
#     text = serializers.CharField()
#     product_id = serializers.IntegerField()
#
#     def validate_product_id(self, product_id):
#         try:
#             Product.objects.get(id=product_id)
#         except Product.DoesNotExist:
#             raise ValidationError('Product not found!')
#         return product_id

class ReviewValidateSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product'
    )

    class Meta:
        model = Review
        fields = ['stars', 'text', 'product_id']
        extra_kwargs = {
            'stars': {'min_value': 1, 'max_value': 5}
        }
