from random import choices
from string import ascii_letters

from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    count = serializers.IntegerField(read_only=True)
    shortened_link = serializers.URLField(read_only=True)
    is_premium = serializers.BooleanField(default=False)
    custom_url = serializers.CharField(allow_null=True, max_length=250)


    class Meta:
        model = Link
        fields = ['id', 'original_link', 'shortened_link', 'created_at', 'count', 'is_premium', 'custom_url']

    def create(self, validated_data):
        url = super().create(validated_data)
        url.save()  # save in db
        random_string = ''.join(choices(ascii_letters, k=6))

        original_link = validated_data.get('original_link')

        if (custom_string := validated_data.get('custom_url')) and validated_data.get('is_premium'):
            random_string = custom_string
            url.is_premium = True

        host = self.context.get('request').headers.get('host')

        if original_link:
            link = 'http://' + host + '/api/' + random_string + '/'
            url.shortened_link = link
            url.save()
        return url
