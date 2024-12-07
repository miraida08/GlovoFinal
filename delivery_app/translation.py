from .models import Store, Category, Product, ProductCombo
from modeltranslation.translator import TranslationOptions, register


@register(Store)
class StoreTranslationOptions(TranslationOptions):
    fields = ('store_name', 'store_description')


@register(Category)
class StoreTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'description')


@register(ProductCombo)
class ProductTranslationOptions(TranslationOptions):
    fields = ('combo_name', 'description')