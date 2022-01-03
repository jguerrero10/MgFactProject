from django.db import models
from django.contrib.auth.models import User


TYPE_CHOICES = [
    ('CC', 'Cedula de ciudadanía'),
    ('NIT', 'Identificación Tributaria')
]


class Client(models.Model):
    """
    This class represents customers

    Attributes:
        :param user : [object] Relationship Field to User Model
        :param id_document: [str] Char Field identification document
        :param id_type: [str] Char Field type of document of identy
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_document = models.CharField(max_length=15, unique=True)
    id_type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
        default='CC'
    )

    def __str__(self):
        return f'{self.user.username} - {self.user.first_name} {self.user.last_name}'


class TypeProduct(models.Model):
    """
        This class represents product

        Attributes:
            :param name: str Char Field product Type name
            :param description: str Description Product
        """
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    """
    This class represents product

    Attributes:
        :param name: str Char Field product name
        :param code: str code product code
        :param price: float Number of the product price
        :param type_product: str product type
    """
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=15, unique=True)
    price = models.FloatField()
    type_product = models.ForeignKey(TypeProduct, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.code} | {self.name} | {self.type_product}'


class Invoice(models.Model):
    """
        This class represents Invoice

        Attributes:
            :param invoice_issuer: [object] Relationship Field to User Generator Invoice
            :param client: [object] Relationship Field to Client
            :param date: [date] invoice generation date
            :param products: [object] Relationship Field to User Generator Invoice
        """
    invoice_issuer = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(
        auto_now=True
    )
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} - {self.client} | {self.invoice_issuer}'
