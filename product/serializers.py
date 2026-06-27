from rest_framework import serializers
from .models import Category, Product, Review


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