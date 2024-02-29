from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from uniconnectapp.models import University, Campus, College, Department, UserProfile, Lecture, Lab, Post, Comment, Rating, Notification, News, Photo, Video, UniversityNews, CampusNews, CollegeNews, DepartmentNews, Course,CampusRegistrationRequest,FriendRequest

# Serializers
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'
class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'

class CampusRegistrationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampusRegistrationRequest
        fields = '__all__'
class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = '__all__'

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'

class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class UniversityNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityNews
        fields = '__all__'

class CampusNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampusNews
        fields = '__all__'

class CollegeNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeNews
        fields = '__all__'

class DepartmentNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentNews
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

# ViewSets

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class CampusViewSet(viewsets.ModelViewSet):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer

class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class LabViewSet(viewsets.ModelViewSet):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class UniversityNewsViewSet(viewsets.ModelViewSet):
    queryset = UniversityNews.objects.all()
    serializer_class = UniversityNewsSerializer

class CampusNewsViewSet(viewsets.ModelViewSet):
    queryset = CampusNews.objects.all()
    serializer_class = CampusNewsSerializer

class CollegeNewsViewSet(viewsets.ModelViewSet):
    queryset = CollegeNews.objects.all()
    serializer_class = CollegeNewsSerializer

class DepartmentNewsViewSet(viewsets.ModelViewSet):
    queryset = DepartmentNews.objects.all()
    serializer_class = DepartmentNewsSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
class CampusRegistrationRequestViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CampusRegistrationRequestSerializer
class FriendRequestViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = FriendRequestSerializer



router = routers.DefaultRouter()
router.register(r'friend-requests', FriendRequestViewSet)
router.register(r'universities', UniversityViewSet)
router.register(r'campuses', CampusViewSet)
router.register(r'colleges', CollegeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'lectures', LectureViewSet)
router.register(r'labs', LabViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'news', NewsViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'universitynews', UniversityNewsViewSet)
router.register(r'campusnews', CampusNewsViewSet)
router.register(r'collegenews', CollegeNewsViewSet)
router.register(r'departmentnews', DepartmentNewsViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'campus-registration-requests', CampusRegistrationRequestViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]