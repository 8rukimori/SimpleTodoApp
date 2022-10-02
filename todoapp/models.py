from turtle import title
from django.db import models

#charfieldのプロパティにchoiceを設定することで、選択式のデータが作れる。
#この際、選択肢はタプルで作成。ソースとなるタプルは大文字で名称設定するのが一般的。
#左側がテンプレートにわたす値、右側にユーザー選択肢
CHOICE = ('danger', 'high'), ('warning', 'normal'), ('primary','low')

class Todo(models.Model):
    title = models.CharField(max_length=60)
    memo = models.TextField(blank=True, null=True,)
    priority = models.CharField(
        max_length=50,
        choices = CHOICE,
    )
    due_date = models.DateField()

    def __str__(self):
        return self.title
