# templates 태그 새로 만들어서 적용하기
from django import template
from usingform.models import CommentLike, Like, Favorite
from account.models import Commentalert, Profile
register = template.Library()

# Board 좋아요 용 확인
@register.filter
def alert_checking(obj , user):
    try:
        print(obj, user)
        getProfile = Profile.objects.get(Name=user) #안됬는데 보니깐 슈퍼유저는 Profile이 안만들어져서 찾지를 못하는 것이였음
        comment_a = Commentalert.objects.get(profile=getProfile)
        if getProfile.alert == comment_a.recent:
            return '<svg class="svg-icon" enable-background="new 0 0 512 512" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="m460.357 344.286h-15c-29.697 0-53.857-24.16-53.857-53.857v-120.542c0-50.626-37.431-92.67-86.071-99.92v-20.538c-.001-27.255-22.174-49.429-49.429-49.429s-49.429 22.174-49.429 49.429v20.538c-48.64 7.25-86.071 49.294-86.071 99.92v120.542c0 29.697-24.16 53.857-53.857 53.857h-15v98.856h154.928v19.429c0 27.255 22.174 49.429 49.429 49.429s49.429-22.174 49.429-49.429v-19.429h154.929v-98.856zm-204.357-314.286c10.713 0 19.429 8.716 19.429 19.429v19.429h-38.857v-19.429c-.001-10.713 8.715-19.429 19.428-19.429zm-105.5 260.429v-120.542c0-39.166 31.864-71.029 71.03-71.029h68.941c39.166 0 71.029 31.863 71.029 71.029v120.542c0 20.489 7.397 39.277 19.647 53.857h-250.294c12.25-14.581 19.647-33.368 19.647-53.857zm124.928 172.142c0 10.713-8.716 19.429-19.429 19.429s-19.429-8.716-19.429-19.429v-19.429h38.857v19.429zm154.929-49.428h-348.714v-38.856h348.714z"/></svg>'
        else:
            return '<svg class="svg-icon" enable-background="new 0 0 512 512" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><g><path d="m292.57 36.57v47.423h-73.14v-47.423c0-20.2 16.37-36.57 36.57-36.57 10.1 0 19.24 4.09 25.86 10.71s10.71 15.76 10.71 25.86z" fill="#feb920"/><path d="m292.57 36.57v47.423h-36.57v-83.993c10.1 0 19.24 4.09 25.86 10.71s10.71 15.76 10.71 25.86z" fill="#fc9b28"/><path d="m292.57 427.676v47.754c0 10.1-4.09 19.24-10.71 25.86s-15.76 10.71-25.86 10.71c-20.2 0-36.57-16.37-36.57-36.57v-47.754z" fill="#ffcf67"/><path d="m292.57 427.676v47.754c0 10.1-4.09 19.24-10.71 25.86s-15.76 10.71-25.86 10.71v-84.324z" fill="#feb920"/><path d="m457.14 375.716-16.01 28h-370.26l-16.01-28c40.39 0 73.14-32.74 73.14-73.14v-148.052c0-50.47 40.91-91.39 91.38-91.39h73.24c50.47 0 91.38 40.92 91.38 91.39v148.053c0 40.399 32.75 73.139 73.14 73.139z" fill="#ffcf67"/><path d="m457.14 375.716-16.01 28h-185.13v-340.582h36.62c50.47 0 91.38 40.92 91.38 91.39v148.053c0 40.399 32.75 73.139 73.14 73.139z" fill="#feb920"/><path d="m54.86 375.716h402.28v73.15h-402.28z" fill="#feb920"/><path d="m256 375.716h201.14v73.15h-201.14z" fill="#fc9b28"/></g></svg>'
            
    except:
        Commentalert.objects.create(profile=getProfile, recent=0)
        return '<svg class="svg-icon" enable-background="new 0 0 512 512" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="m460.357 344.286h-15c-29.697 0-53.857-24.16-53.857-53.857v-120.542c0-50.626-37.431-92.67-86.071-99.92v-20.538c-.001-27.255-22.174-49.429-49.429-49.429s-49.429 22.174-49.429 49.429v20.538c-48.64 7.25-86.071 49.294-86.071 99.92v120.542c0 29.697-24.16 53.857-53.857 53.857h-15v98.856h154.928v19.429c0 27.255 22.174 49.429 49.429 49.429s49.429-22.174 49.429-49.429v-19.429h154.929v-98.856zm-204.357-314.286c10.713 0 19.429 8.716 19.429 19.429v19.429h-38.857v-19.429c-.001-10.713 8.715-19.429 19.428-19.429zm-105.5 260.429v-120.542c0-39.166 31.864-71.029 71.03-71.029h68.941c39.166 0 71.029 31.863 71.029 71.029v120.542c0 20.489 7.397 39.277 19.647 53.857h-250.294c12.25-14.581 19.647-33.368 19.647-53.857zm124.928 172.142c0 10.713-8.716 19.429-19.429 19.429s-19.429-8.716-19.429-19.429v-19.429h38.857v19.429zm154.929-49.428h-348.714v-38.856h348.714z"/></svg>'