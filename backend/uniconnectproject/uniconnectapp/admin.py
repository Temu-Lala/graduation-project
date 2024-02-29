from django.contrib import admin
from .models import University, Campus, College, Department, UserProfile, Lecture, Lab, \
                    Post, Comment, Rating, Notification, News, Photo, Video, UniversityNews, \
                    CampusNews, CollegeNews, DepartmentNews, Course,CampusRegistrationRequest,FriendRequest

admin.site.register(University)
admin.site.register(Campus)
admin.site.register(College)
admin.site.register(Department)
admin.site.register(UserProfile)
admin.site.register(Lecture)
admin.site.register(Lab)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Notification)
admin.site.register(News)
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(UniversityNews)
admin.site.register(CampusNews)
admin.site.register(CollegeNews)
admin.site.register(DepartmentNews)
admin.site.register(Course)
admin.site.register(CampusRegistrationRequest)
admin.site.register(FriendRequest)

