from django.db import models


class Daibunrui(models.Model):
    """大分類 (A-T, 20 items)"""

    code = models.CharField(max_length=1, primary_key=True)  # A, B, C...
    name = models.CharField(max_length=100)  # 農業，林業

    class Meta:
        ordering = ["code"]
        verbose_name = "大分類"
        verbose_name_plural = "大分類"

    def __str__(self):
        return f"{self.code} {self.name}"


class Chubunrui(models.Model):
    """中分類 (~200 items)"""

    code = models.CharField(max_length=3, primary_key=True)  # 09, 10, 11...
    name = models.CharField(max_length=100)  # 食料品製造業
    daibunrui = models.ForeignKey(
        Daibunrui, on_delete=models.CASCADE, related_name="chubunrui_list"
    )

    class Meta:
        ordering = ["code"]
        verbose_name = "中分類"
        verbose_name_plural = "中分類"

    def __str__(self):
        return f"{self.code} {self.name}"


class Shobunrui(models.Model):
    """小分類 (~1,000 items)"""

    code = models.CharField(max_length=4, primary_key=True)  # 091, 092...
    name = models.CharField(max_length=100)  # 畜産食料品製造業
    chubunrui = models.ForeignKey(
        Chubunrui, on_delete=models.CASCADE, related_name="shobunrui_list"
    )

    class Meta:
        ordering = ["code"]
        verbose_name = "小分類"
        verbose_name_plural = "小分類"

    def __str__(self):
        return f"{self.code} {self.name}"
