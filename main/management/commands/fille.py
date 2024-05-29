from django.core.management import BaseCommand
from main.models import Category, Product
import json


class Command(BaseCommand):

    @staticmethod
    def json_read(file_name):
        with open(file_name, encoding='utf-8') as json_file:
            return json.load(json_file)

    def handle(self, *args, **options):
        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте категории
        categories_data = Command.json_read('category.json')
        category_map = {}
        for category_data in categories_data:
            category = Category.objects.create(
                name=category_data['fields']['name'],
                description=category_data['fields']['description']
            )
            category_map[category_data['pk']] = category

        # Создайте продукты
        products_data = Command.json_read('product.json')
        for product_data in products_data:
            category_id = product_data['fields']['category']
            if category_id in category_map:
                Product.objects.create(
                    name=product_data['fields']['name'],
                    description=product_data['fields']['description'],
                    price=product_data['fields']['price'],
                    category=category_map[category_id]
                )
            else:
                print(f"Category with id {category_id} does not exist.")
