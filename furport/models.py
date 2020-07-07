from django.db import models


class Tag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField("タグ名", max_length=255, blank=False, default="")
    group = models.CharField("タググループ", max_length=255, blank=False, default="")
    description = models.TextField("詳細", blank=True, default="")

    class Meta:
        ordering = ("name",)


class Event(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField("イベント名", max_length=255, blank=False, default="")
    start_datetime = models.DateTimeField("開始時刻")
    end_datetime = models.DateTimeField("終了時刻")
    url = models.CharField("URL", max_length=255, blank=True, default="")
    image_url = models.CharField("画像URL", max_length=255, blank=True, default="")
    description = models.TextField("詳細", blank=True, default="")
    tag = models.ManyToManyField(Tag, blank=True)
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    class Meta:
        ordering = (
            "start_datetime",
            "end_datetime",
        )
