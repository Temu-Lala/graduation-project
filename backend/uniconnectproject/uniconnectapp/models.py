from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

class FriendRequest(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
    )

    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    sent_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('from_user', 'to_user'),)

    def __str__(self):
        return f"{self.from_user} -> {self.to_user} ({self.status})"

class University(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    founded_year = models.PositiveIntegerField(blank=True, null=True)
    website = models.URLField(blank=True)
    cover_photo = models.ImageField(upload_to='university_covers/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Campus(models.Model):
    name = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class CampusRegistrationRequest(models.Model):
    campus = models.OneToOneField(Campus, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)

@receiver(post_save, sender=CampusRegistrationRequest)
def campus_registration_notification(sender, instance, created, **kwargs):
    if created and instance.is_accepted:
        # Send notification to university admin for approval
        university_admin = instance.campus.university.admin
        subject = f"Campus Registration Approval: {instance.campus.name}"
        message = f"Campus {instance.campus.name} has sent a registration request and is awaiting approval.\n"\
                  f"Visit the admin panel to approve or decline."
        from_email = "admin@example.com"  # Replace with your admin email
        send_mail(subject, message, from_email, [university_admin.email])

    # You can handle other actions based on acceptance or rejection if needed

class College(models.Model):
    name = models.CharField(max_length=255)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)
    head = models.ForeignKey(User, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    achievements = models.TextField()
    projects = models.TextField()
    profile_photo = models.ImageField(upload_to='profile_photos/')
    bio = models.TextField(blank=True)
    education = models.CharField(max_length=255, blank=True)
    work_experience = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    linkedin_profile = models.URLField(blank=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)

    def __str__(self):
        return self.user.username

class Lecture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    education = models.CharField(max_length=255, blank=True)
    experience = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    linkedin_profile = models.URLField(blank=True)
    profile_photo = models.ImageField(upload_to='lecture_profile_photos/', blank=True, null=True)
    courses_taught = models.ManyToManyField('Course', related_name='lecturers', blank=True)

    def __str__(self):
        return self.user.username

class Lab(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    lab_assistant = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    photo = models.ImageField(upload_to='post_photos/', blank=True, null=True)
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    comments = models.ManyToManyField('Comment', related_name='post_comments', blank=True)

    def __str__(self):
        return f"Post by {self.user.username}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username}"

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"Rating by {self.user.username} for {self.university.name}"

class Notification(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_notifications')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification to {self.user.username}"

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    photos = models.ManyToManyField('Photo', related_name='news_photos', blank=True)
    videos = models.ManyToManyField('Video', related_name='news_videos', blank=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, blank=True, null=True)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, blank=True, null=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    image = models.ImageField(upload_to='news_photos/')

class Video(models.Model):
    video_file = models.FileField(upload_to='news_videos/')

class UniversityNews(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

class CampusNews(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

class CollegeNews(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

class DepartmentNews(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

class Course(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name='enrolled_courses', blank=True)

    def __str__(self):
        return self.name
