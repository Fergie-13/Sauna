from django.db import models



class Besedka(models.Model):
    name = models.CharField(
        verbose_name = "Besedka's name",
        max_length = 30,
    )
    description = models.TextField(
        verbose_name = "Besedka's description",
        blank = True,
        null = True
    )
    fire = models.TextField(
        verbose_name = "Fire's description",
        blank = True,
        null = True
    )
    tools = models.TextField(
        verbose_name = "Tools description",
        blank = True,
        null = True
    )
    area = models.TextField(
        verbose_name = "Area's description",
        blank = True,
        null = True
    )
    parking = models.TextField(
        verbose_name = "Parking's description",
        blank = True,
        null = True
    )

    def __str__(self) -> str:
        return self.name


class Billiard(models.Model):
    name = models.CharField(
        verbose_name = "Billiard's name",
        max_length = 30,
    )
    par = models.TextField(
        verbose_name = "Par description",
        blank = True,
        null = True
    )
    water = models.TextField(
        verbose_name = "Water description",
        blank = True,
        null = True
    )
    rest = models.TextField(
        verbose_name = "Rest description",
        blank = True,
        null = True
    )
    extra = models.TextField(
        verbose_name = "Extra description",
        blank = True,
        null = True
    )
    besedka = models.ManyToManyField(
        'list.Besedka',
        verbose_name="Besedka",
        related_name="besedkas"
    )

    def __str__(self) -> str:
        return self.name



class Pool(models.Model):
    name = models.CharField(
        verbose_name = "Pool's name",
        max_length = 30,
    )
    par = models.TextField(
        verbose_name = "Par description",
        blank = True,
        null = True
    )
    water = models.TextField(
        verbose_name = "Water description",
        blank = True,
        null = True
    )
    rest = models.TextField(
        verbose_name = "Rest description",
        blank = True,
        null = True
    )
    extra = models.TextField(
        verbose_name = "Extra description",
        blank = True,
        null = True
    )
    besedka = models.ManyToManyField(
        'list.Besedka',
        verbose_name="Besedca",
        related_name="besedcas"
    )

    def __str__(self) -> str:
        return self.name
