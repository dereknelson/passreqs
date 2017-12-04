from rest_framework import serializers
from .models import Website, PassReqs

class WebsiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Website
        fields = ('id', 'url', 'created_at',
                  'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at',)

    def create(self, validated_data):
        try:
            #this def needs editing
            existing_website = Website.objects.get(website=self.context['request'].user, url=validated_data['url'])
        except Website.DoesNotExist:
            existing_website = Website.objects.get(website=self.context['request'].user, url=validated_data['url'])
            return Website(**validated_data)
        except Website.DoesExist:
            raise serializers.ValidationError("Record for this URL already exists, try updating.")

class PassreqsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PassReqs
        fields = ('website', 'length', 'special_characters', 'capitals', 'complex', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'created_at', 'updated_at')