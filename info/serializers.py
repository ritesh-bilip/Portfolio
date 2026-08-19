from rest_framework import serializers
from .models import Certification, ContactMessage, Education, Profile, Project, Skill


class ProfileSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()
    resume_file = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'full_name', 'tagline', 'summary', 'email', 'phone', 'location',
            'github_url', 'linkedin_url', 'extra_link_label', 'extra_link_url',
            'extracurricular', 'is_open_to_work', 'profile_image', 'resume_file',
        ]

    def _absolute(self, file_field):
        if not file_field:
            return None
        request = self.context.get('request')
        url = file_field.url
        return request.build_absolute_uri(url) if request else url

    def get_profile_image(self, obj):
        return self._absolute(obj.profile_image)

    def get_resume_file(self, obj):
        return self._absolute(obj.resume_file)


class SkillSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = Skill
        fields = ['id', 'name', 'category', 'category_display', 'icon', 'proficiency', 'order']


class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'short_description', 'detailed_description',
            'tech_stack', 'github_url', 'live_url', 'image', 'is_featured',
            'order', 'created_at',
        ]

    def get_image(self, obj):
        if not obj.image:
            return None
        request = self.context.get('request')
        url = obj.image.url
        return request.build_absolute_uri(url) if request else url


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'degree', 'institution', 'board_or_note', 'period', 'order']


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ['id', 'title', 'issuer', 'credential_id', 'issue_date', 'credential_url', 'order','certificate_image']


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'subject', 'message', 'created_at']