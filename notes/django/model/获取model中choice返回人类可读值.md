## choice参数
该参数接收一个可迭代的列表或元组（基本单位为二元组）。如果指定了该参数，在实例化该模型时，该字段只能取选项列表中的值。

### Model.get_FOO_display()


- 每个二元组的第一个值会储存在数据库中，而第二个值将只会用于显示作用。

- 对于一个模型实例，要获取该字段二元组中相对应的第二个值，使用get_FOO_display()方法,其中FOO是字段的名称。此方法返回字段的“人类可读”值。

例如：
```
from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=2, choices=SHIRT_SIZES)

>>> p = Person(name="Fred Flintstone", shirt_size="L")
>>> p.save()
>>> p.shirt_size
'L'
>>> p.get_shirt_size_display()
'Large'
```
