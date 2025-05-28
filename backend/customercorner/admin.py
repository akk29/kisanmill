from django.contrib import admin
from .models import Product , PreProductInfo, BadQualityCondition , GoodQualityCondition, NutrionalContent , Product_type , CultivationMethods

admin.site.register(CultivationMethods)
admin.site.register(Product)
admin.site.register(PreProductInfo)
admin.site.register(NutrionalContent)
admin.site.register(BadQualityCondition)
admin.site.register(GoodQualityCondition)
admin.site.register(Product_type)
