# Generated by Django 4.2.3 on 2023-07-21 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake_app', '0004_readycake_topping_alter_customizedcake_berries_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customizedcake',
            name='berries',
            field=models.CharField(choices=[('Без ягод', 'Без ягод'), ('Ежевика', 'Ежевика'), ('Малина', 'Малина'), ('Голубика', 'Голубика'), ('Клубника', 'Клубника')], default='Без ягод', max_length=50, verbose_name='Ягоды'),
        ),
        migrations.AlterField(
            model_name='customizedcake',
            name='decore',
            field=models.CharField(choices=[('Без декора', 'Без декора'), ('Фисташки', 'Фисташки'), ('Безе', 'Безе'), ('Фундук', 'Фундук'), ('Пекан', 'Пекан'), ('Маршмеллоу', 'Маршмеллоу'), ('Марципан', 'Марципан')], default='Без декора', max_length=50, verbose_name='Декор'),
        ),
        migrations.AlterField(
            model_name='readycake',
            name='topping',
            field=models.CharField(choices=[('Без топпинга', 'Без топпинга'), ('Белый соус', 'Белый соус'), ('Карамельный сироп', 'Карамельный сироп'), ('Кленовый сироп', 'Кленовый сироп'), ('Клубничный сироп', 'Клубничный сироп'), ('Черничный сироп', 'Черничный сироп'), ('Молочный шоколад', 'Молочный шоколад')], default='Без топпинга', max_length=50, verbose_name='Топпинг'),
        ),
    ]
