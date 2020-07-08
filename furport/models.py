from django.db import models


class TagGroup(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField("タググループ名", max_length=255, blank=False, default="")
    color = models.CharField("タグ色", max_length=255, blank=False, default="")
    priority = models.IntegerField("優先度", blank=False, default=0)
    description = models.TextField("詳細", blank=True, default="")

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Tag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField("タグ名", max_length=255, blank=False, default="")
    group = models.ForeignKey(TagGroup, on_delete=models.CASCADE)
    description = models.TextField("詳細", blank=True, default="")

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Event(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField("イベント名", max_length=255, blank=False, default="")
    start_datetime = models.DateTimeField("開始時刻")
    end_datetime = models.DateTimeField("終了時刻")
    url = models.CharField("URL", max_length=255, blank=True, default="")
    twitter_id = models.CharField("TwitterId", max_length=255, blank=True, default="")
    description = models.TextField("詳細", blank=True, default="")
    tag = models.ManyToManyField(Tag, blank=True)
    created_by = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="created_by"
    )
    stared_by = models.ManyToManyField(
        "auth.User", blank=True, related_name="stared_by"
    )

    class Meta:
        ordering = (
            "start_datetime",
            "end_datetime",
        )

    def __str__(self):
        return self.name
