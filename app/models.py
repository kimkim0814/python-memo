from django.db import models

from users.models import User


class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    # task
    task = models.CharField(
        verbose_name='やること',
        max_length=20,
        blank=True,
        null=True,
    )

    # 内容
    content = models.TextField(
        verbose_name='内容',
        blank=True,
        null=True,
    )

    # サンプル項目7 日付
    start = models.DateTimeField(
        verbose_name='いつから',
        blank=True,
        null=True,
    )
    # サンプル項目8 日時
    end = models.DateTimeField(
        verbose_name='いつまでに',
        blank=True,
        null=True,
    )

    # サンプル項目9 選択肢（固定）
    sample_9_choice = (
        (1, '重要度高'),
        (2, '重要度中'),
        (3, '重要度低'),
    )

    sample_9 = models.IntegerField(
        verbose_name='タスクの重要度',
        choices=sample_9_choice,
        blank=True,
        null=True,
    )

    # サンプル項目9 選択肢（マスタ連動）
    sample_10 = models.ForeignKey(
        User,
        verbose_name='誰のタスクか',
        blank=True,
        null=True,
        related_name='sample_10',
        on_delete=models.SET_NULL,
    )

    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.task

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'チーム開発タスク管理アプリ'
        verbose_name_plural = 'チーム開発タスク管理アプリ'
