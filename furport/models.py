from django.db import models
from django.dispatch import receiver


class GeneralTag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField("タグ名", max_length=255, blank=False, default="")
    description = models.TextField("詳細", blank=True, default="")

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class CharacterTag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField("タグ名", max_length=255, blank=False, default="")
    description = models.TextField("詳細", blank=True, default="")

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class OrganizationTag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField("タグ名", max_length=255, blank=False, default="")
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
    timezone = models.CharField(
        "IANAタイムゾーン名", max_length=255, blank=True, default="Asia/Tokyo"
    )
    no_time = models.BooleanField("時間未定フラグ", blank=True, default=False)
    url = models.CharField("URL", max_length=255, blank=True, default="")
    twitter_id = models.CharField("TwitterId", max_length=255, blank=True, default="")
    description = models.TextField("詳細", blank=True, default="")
    country = models.CharField("国名", max_length=255, blank=False, default="")
    state = models.CharField("都道府県・州名", max_length=255, blank=False, default="")
    city = models.CharField("市名", max_length=255, blank=True, default="")
    place = models.CharField("会場名", max_length=255, blank=True, default="")
    google_map_description = models.CharField(
        "グーグルマップ位置情報ワード", max_length=255, blank=True, default=""
    )
    google_map_place_id = models.CharField(
        "グーグルマップ位置情報id", max_length=255, blank=True, default=""
    )
    attendees = models.IntegerField("参加者数", blank=True, default=0)
    openness = models.IntegerField("公開度", blank=True, default=0)
    search_keywords = models.TextField("検索キーワード", blank=True, default="")
    general_tag = models.ManyToManyField(GeneralTag, blank=True)
    character_tag = models.ManyToManyField(CharacterTag, blank=True)
    organization_tag = models.ManyToManyField(OrganizationTag, blank=True)
    created_by = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="created_by"
    )

    class Meta:
        ordering = ("start_datetime", "end_datetime")

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, primary_key=True)
    star = models.ManyToManyField(Event, blank=True, related_name="star")
    attend = models.ManyToManyField(Event, blank=True, related_name="attend")
    following = models.ManyToManyField(
        "self", blank=True, related_name="follower", symmetrical=False
    )
    avatar = models.CharField("アバター画像URL", max_length=255, blank=True, default="")
    twitter_id = models.CharField("TwitterID", max_length=255, blank=True, default="")
    location = models.CharField("場所", max_length=255, blank=True, default="")
    is_moderator = models.BooleanField("モデレータフラグ", blank=True, default=False)
    description = models.TextField("詳細", blank=True, default="")

    class Meta:
        ordering = ("user",)

    def __str__(self):
        return "%s profile" % self.user.username
