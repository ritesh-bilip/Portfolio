from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify


class Profile(models.Model):
    full_name = models.CharField(max_length=150, default="Ritesh Kumar Das")
    tagline = models.CharField(
        max_length=200,
        default="Django Backend Developer | Python",
        help_text="Short title shown under your name in the hero section.",
    )
    summary = models.TextField(help_text="Professional summary shown in the About section.")
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=100, blank=True, default="India")

    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    extra_link_label = models.CharField(
        max_length=50, blank=True, help_text="Optional label for a third link, e.g. 'LeetCode'."
    )
    extra_link_url = models.URLField(blank=True)

    extracurricular = models.TextField(
        blank=True,
        help_text="E.g. cricket / sports / society achievements shown on the About section.",
    )
    is_open_to_work = models.BooleanField(
        default=True,
        help_text="Shows an 'open to work' badge in the hero.",
    )

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(
            pk=1,
            defaults={
                'email': 'riteshkrdas479@gmail.com',
                'summary': 'Django Backend Developer specialization in building scalable REST APIs.',
            },
        )
        return obj


class Skill(models.Model):
    class Category(models.TextChoices):
        BACKEND = 'backend', 'Backend'
        LANGUAGES = 'languages', 'Languages'
        API_AUTH = 'api_auth', 'APIs & Auth'
        DATABASES = 'databases', 'Databases'
        FRONTEND = 'frontend', 'Frontend'
        TOOLS = 'tools', 'Tools'
        CS_FUNDAMENTALS = 'cs_fundamentals', 'CS Fundamentals'
        SOFT_SKILLS = 'soft_skills', 'Soft Skills'

    name = models.CharField(max_length=80)
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.BACKEND)
    icon = models.CharField(
        max_length=50, blank=True,
        help_text="Optional react-icons name, e.g. 'SiDjango', 'SiPostgresql', 'FaPython'.",
    )
    proficiency = models.PositiveSmallIntegerField(
        blank=True, null=True,
        help_text="Optional 0-100 self-rating.",
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True, blank=True)
    short_description = models.CharField(
        max_length=300,
        help_text="One or two sentences shown on the project card.",
    )
    detailed_description = models.TextField(blank=True)
    tech_stack = models.JSONField(
        default=list, blank=True,
        help_text='List of technology tags, e.g. ["Django", "PostgreSQL", "Redis"].',
    )
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', 'order', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                counter += 1
                slug = f"{base_slug}-{counter}"
            self.slug = slug
        super().save(*args, **kwargs)


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    board_or_note = models.CharField(max_length=200, blank=True)
    period = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} — {self.institution}"


class Certification(models.Model):
    title = models.CharField(max_length=150)
    issuer = models.CharField(max_length=150, blank=True)
    credential_id = models.CharField(max_length=150, blank=True)
    issue_date = models.CharField(max_length=50)
    credential_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    certificate_image = models.ImageField(upload_to='cerificate/', blank=True, null=True)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} ({self.email})"