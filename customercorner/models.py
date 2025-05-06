from django.db import models

class Product_type(models.Model):
    name = models.CharField(max_length=15,null=False,blank=False)
    image = models.ImageField()

    def __str__(self):
        return self.name

class Product(models.Model):

    Product_name = models.CharField(max_length = 10, blank = False , null = False)
    Product_type = models.ForeignKey(Product_type,on_delete=models.CASCADE)
    Product_version = models.CharField(max_length = 15, blank = False , null = False)
    Product_Images = models.ImageField()


    def __str__(self):
        return self.Product_name + ' -- ' + self.Product_version

    @property
    def Product_typ(self):
        return str(self.Product_type).capitalize()

    @property
    def version(self):
        return self.Product_version

    def productwithversion(self):
        return str(self.Product_version) +" " + str(self.Product_name)


    ''' This method can be called in the template to get the value related in the other table'''
    def preproductinfo(self):
        return PreProductInfo.objects.filter(Select_Product=self)

    def NutrionalContent(self):
        return NutrionalContent.objects.filter(Select_Product = self)


    def GoodQualityCondition(self):
        return GoodQualityCondition.objects.filter(Select_Product = self)

    def BadQualityCondition(self):
        return BaddQualityCondition.objects.filter(Select_Product = self)

    def all_productinfo(self):
        return self.pk.PreProductInfo_set.all()

    def all_pre_productinfo(self):
        return self.PreProductInfo_set.all()

    def get_image(self):
        self.Product_Images.url


class PreProductInfo(models.Model):
    Seasons_list = (
    ('Summer','Summer'),
    ('Winter','Winter')
    )
    Soil_Choices = (
    ('alluvial','Alluvial'),
    ('loamy','Loamy')
    )
    Select_Product = models.ForeignKey(Product,on_delete=models.CASCADE,default = None)
    Season = models.CharField(max_length = 10 , choices = Seasons_list,default=None)
    Soil_type = models.CharField(max_length = 10 , choices = Soil_Choices,default = None)
    Investment_cost = models.IntegerField(blank = False,null=False)



    def __str__(self):
        return self.Select_Product.Product_name + ' -- '+ str(self.Season).capitalize() + '--' + str(self.Soil_type).capitalize()

    @property
    def cost(self):
        return str(self.Investment_cost) + ' RS/-'

    @property
    def soil(self):
        return str(self.Soil_type).capitalize()

class NutrionalContent(models.Model):
    Select_Product = models.ForeignKey(Product,on_delete=models.CASCADE,default = None)
    # NutrionalData = models.TextField(max_length=1500,help_text='Please seprate the Nutrional Content by comma\'s',null=False,blank=False)
    ConsumptionEffect = models.TextField(max_length=1500,help_text='Please seprate the Consumption Effect by comma\'s',null=False,blank=False)

    NutrionChart = models.ImageField()

    Fat = models.IntegerField()
    Carbohydrates = models.IntegerField()
    Protein = models.IntegerField()
    Sugar = models.IntegerField()

    def __str__(self):
        return "Nutrional content -- " + str(self.Select_Product.Product_version) + " " + str(self.Select_Product.Product_name)

class GoodQualityCondition(models.Model):
    Select_Product = models.ForeignKey(Product,on_delete=models.CASCADE,default = None)
    CheckingConditions = models.TextField(max_length=1500,help_text='Please seprate the Good Conditions of the Product by comma\'s',null=False,blank=False)
    Good_Images = models.ImageField()

class BadQualityCondition(models.Model):
    Select_Product = models.ForeignKey(Product,on_delete=models.CASCADE,default = None)
    CheckingConditions = models.TextField(max_length=1500,help_text='Please seprate the Good Conditions of the Product by comma\'s',null=False,blank=False)
    Good_Images = models.ImageField()


class CultivationMethods(models.Model):
    Seasons_list = (
    ('Summer','Summer'),
    ('Winter','Winter')
    )
    Soil_Choices = (
    ('alluvial','Alluvial'),
    ('loamy','Loamy')
    )
    Select_Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Description = models.CharField(max_length = 1500)
    Investment_cost = models.IntegerField()
    Season = models.CharField(max_length = 10 , choices = Seasons_list,default=None)
    Soil_type = models.CharField(max_length = 10 , choices = Soil_Choices,default = None)
