from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from . import models
import json

# Create your views here.


@csrf_exempt
def create_profile_api(request):
    if request.method == "POST":
        parsed_data = JSONParser().parse(request)
        user_profile = models.UserProfile()
        user_profile.Username = parsed_data.get('Username')
        user_profile.FirstName = parsed_data.get('FirstName')
        user_profile.LastName = parsed_data.get('LastName')
        if parsed_data.get('ProfileImage'):
            user_profile.ProfileImage = parsed_data.get('ProfileImage')
        user_profile.save()
        return JsonResponse("User Profile Created Successfully !!!", safe=False)
    return JsonResponse("Illegal Operation. Only POST for create profile expected.", safe=False)


@csrf_exempt
def get_profile_api(request, id=0):
    if request.method == "GET":
        try:
            user_profile = models.UserProfile.objects.get(ProfileId=id)
        except:
            return JsonResponse("Profile you are trying to access does not exist.", safe=False)
        data = {
            "ProfileId": user_profile.ProfileId,
            "Username": user_profile.Username,
            "FirstName": user_profile.FirstName,
            "LastName": user_profile.LastName,
        }
        if user_profile.ProfileImage != None:
            data['ProfileImage'] = str(user_profile.ProfileImage)
        return JsonResponse(data, safe=False)
    return JsonResponse("Illegal Operation. Only GET for a particular profile expected.", safe=False)


@csrf_exempt
def create_comment_api(request):
    if request.method == "POST":
        parsed_data = JSONParser().parse(request)
        comment = models.PostComment()
        comment.CommentText = parsed_data.get("CommentText")
        commentor_id = parsed_data.get("CommentorId")
        try:
            commentor = models.UserProfile.objects.get(ProfileId=commentor_id)
            comment.CommentorId = commentor.ProfileId
            comment.save()
            return JsonResponse("Comment Posted Successfully !!!", safe=False)
        except:
            comment.CommentorId = 0
            comment.save()
            return JsonResponse("Comment Id provided is not a valid user to saving comment anonymously. Comment Posted Successfully !!!", safe=False)
    return JsonResponse("Illegal Operation. Only Comment POST allowed.", safe=False)


@csrf_exempt
def get_comment_api(request, id=0):
    if request.method == "GET":
        try:
            comment = models.PostComment.objects.get(CommentId=id)
        except:
            return JsonResponse("Comment you are trying to get does not exist.", safe=False)
        if comment.LikedBy != "":
            liked_by = list(map(int, comment.LikedBy.split(";")))
            liker_list = []
            for liker in liked_by:
                try:
                    person = models.UserProfile.objects.get(ProfileId=liker)
                    liker_list.append(person.Username)
                except:
                    liker_list.append("Anonymous")
        else:
            liker_list = []
        if comment.DislikedBy != "":
            disliked_by = list(map(int, comment.DislikedBy.split(";")))
            disliker_list = []
            for disliker in disliked_by:
                try:
                    person = models.UserProfile.objects.get(ProfileId=disliker)
                    disliker_list.append(person.Username)
                except:
                    disliker_list.append("Anonymous")
        else:
            disliker_list = []
        comment_object = {
            "CommentId": comment.CommentId,
            "CommentText": comment.CommentText,
            "Likes": comment.Likes,
            "LikedBy": liker_list,
            "Dislikes": comment.Dislikes,
            "DislikedBy": disliker_list,
            "CommentorId": comment.CommentorId
        }
        return JsonResponse(comment_object, safe=False)
    return JsonResponse("Illegal Operation. Only Comment GET allowed with a particular CommentId.", safe=False)


@csrf_exempt
def get_all_comments_api(request):
    if request.method == "GET":
        all_comments = models.PostComment.objects.all()
        try:
            parsed_data = JSONParser().parse(request)
        except:
            comments = {}
            for comment in all_comments:
                if comment.LikedBy != "":
                    liked_by = list(map(int, comment.LikedBy.split(";")))
                    liker_list = []
                    for liker in liked_by:
                        try:
                            person = models.UserProfile.objects.get(
                                ProfileId=liker)
                            liker_list.append(person.Username)
                        except:
                            liker_list.append("Anonymous")
                else:
                    liker_list = []
                if comment.DislikedBy != "":
                    disliked_by = list(map(int, comment.DislikedBy.split(";")))
                    disliker_list = []
                    for disliker in disliked_by:
                        try:
                            person = models.UserProfile.objects.get(
                                ProfileId=disliker)
                            disliker_list.append(person.Username)
                        except:
                            disliker_list.append("Anonymous")
                else:
                    disliker_list = []
                comments[comment.CommentId] = {
                    'CommentText': comment.CommentText,
                    'Likes': comment.Likes,
                    'LikedBy': liker_list,
                    'Dislikes': comment.Dislikes,
                    'DislikedBy': disliker_list,
                    'CommentorId': comment.CommentorId
                }
            return JsonResponse(comments, safe=False)
        if parsed_data.get('FilterCriteria'):
            if parsed_data.get('FilterCriteria').get('Field').upper() == 'COMMENTID':
                if parsed_data.get('FilterCriteria').get('Operation') == '>' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(CommentId__gt=int(
                        parsed_data.get('FilterCriteria').get('Value')))
                if parsed_data.get('FilterCriteria').get('Operation') == '>=' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(CommentId__gte=int(
                        parsed_data.get('FilterCriteria').get('Value')))
                if parsed_data.get('FilterCriteria').get('Operation') == '<' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(CommentId__lt=int(
                        parsed_data.get('FilterCriteria').get('Value')))
                if parsed_data.get('FilterCriteria').get('Operation') == '<=' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(CommentId__lte=int(
                        parsed_data.get('FilterCriteria').get('Value')))
                if parsed_data.get('FilterCriteria').get('Operation') == 'in' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(
                        CommentId__in=parsed_data.get('FilterCriteria').get('Value'))
            if parsed_data.get('FilterCriteria').get('Field').upper() == 'COMMENTTEXT':
                if parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(CommentText__contains=str(
                        parsed_data.get('FilterCriteria').get('Value')))
            if parsed_data.get('FilterCriteria').get('Field').upper() == 'LIKES':
                if parsed_data.get('FilterCriteria').get('Operation') == '>' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(Likes__gt=int(
                        parsed_data.get('FilterCriteria').get('Value')))
                if parsed_data.get('FilterCriteria').get('Operation') == '>=' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(Likes__gte=int(
                        parsed_data.get('FilterCriteria').get('Value')))
                if parsed_data.get('FilterCriteria').get('Operation') == '<' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(Likes__lt=int(
                        parsed_data.get('FilterCriteria').get('Value')))
                if parsed_data.get('FilterCriteria').get('Operation') == '<=' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(Likes__lte=int(
                        parsed_data.get('FilterCriteria').get('Value')))
                if parsed_data.get('FilterCriteria').get('Operation') == 'in' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(
                        Likes__in=parsed_data.get('FilterCriteria').get('Value'))
            if parsed_data.get('FilterCriteria').get('Field').upper() == 'DISLIKES':
                if parsed_data.get('FilterCriteria').get('Operation') == '>' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(Dislikes__gt=int(
                        parsed_data.get('FilterCriteria').get('Value')))
                if parsed_data.get('FilterCriteria').get('Operation') == '>=' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(Dislikes__gte=int(
                        parsed_data.get('FilterCriteria').get('Value')))
                if parsed_data.get('FilterCriteria').get('Operation') == '<' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(Dislikes__lt=int(
                        parsed_data.get('FilterCriteria').get('Value')))
                if parsed_data.get('FilterCriteria').get('Operation') == '<=' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(Dislikes__lte=int(
                        parsed_data.get('FilterCriteria').get('Value')))
                if parsed_data.get('FilterCriteria').get('Operation') == 'in' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(
                        Dislikes__in=parsed_data.get('FilterCriteria').get('Value'))
            if parsed_data.get('FilterCriteria').get('Field').upper() == 'COMMENTORID':
                if parsed_data.get('FilterCriteria').get('Operation') == '>' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(CommentorId__gt=int(
                        parsed_data.get('FilterCriteria').get('Value')))
                if parsed_data.get('FilterCriteria').get('Operation') == '>=' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(CommentorId__gte=int(
                        parsed_data.get('FilterCriteria').get('Value')))
                if parsed_data.get('FilterCriteria').get('Operation') == '<' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(CommentorId__lt=int(
                        parsed_data.get('FilterCriteria').get('Value')))
                if parsed_data.get('FilterCriteria').get('Operation') == '<=' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(CommentorId__lte=int(
                        parsed_data.get('FilterCriteria').get('Value')))
                if parsed_data.get('FilterCriteria').get('Operation') == 'in' and parsed_data.get('FilterCriteria').get('Value'):
                    all_comments = all_comments.filter(
                        CommentorId__in=parsed_data.get('FilterCriteria').get('Value'))
        if parsed_data.get('SortCriteria'):
            if parsed_data.get('SortCriteria').get('Sort').upper() in ['ASC', 'ASCENDING'] and parsed_data.get('SortCriteria').get('Field').upper() in ['COMMENTID', 'COMMENTTEXT', 'LIKES', 'LIKEDBY', 'DISLIKES', 'DISLIKEDBY', 'COMMENTORID']:
                all_comments = all_comments.order_by(
                    parsed_data.get('SortCriteria').get('Field')).values()
            elif parsed_data.get('SortCriteria').get('Sort').upper() in ['DESC', 'DESCENDING'] and parsed_data.get('SortCriteria').get('Field').upper() in ['COMMENTID', 'COMMENTTEXT', 'LIKES', 'LIKEDBY', 'DISLIKES', 'DISLIKEDBY', 'COMMENTORID']:
                all_comments = all_comments.order_by('-' +
                                                     parsed_data.get('SortCriteria').get('Field')).values()
        comments = {}
        for comment in all_comments:
            if comment.get('LikedBy') != "":
                liked_by = list(map(int, comment.get('LikedBy').split(";")))
                liker_list = []
                for liker in liked_by:
                    try:
                        person = models.UserProfile.objects.get(
                            ProfileId=liker)
                        liker_list.append(person.Username)
                    except:
                        liker_list.append("Anonymous")
            else:
                liker_list = []
            if comment.get('DislikedBy') != "":
                disliked_by = list(
                    map(int, comment.get('DislikedBy').split(";")))
                disliker_list = []
                for disliker in disliked_by:
                    try:
                        person = models.UserProfile.objects.get(
                            ProfileId=disliker)
                        disliker_list.append(person.Username)
                    except:
                        disliker_list.append("Anonymous")
            else:
                disliker_list = []
            comments[comment.get('CommentId')] = {
                'CommentText': comment.get('CommentText'),
                'Likes': comment.get('Likes'),
                'LikedBy': liker_list,
                'Dislikes': comment.get('Dislikes'),
                'DislikedBy': disliker_list,
                'CommentorId': comment.get('CommentorId')
            }
        return JsonResponse(comments, safe=False)
    return JsonResponse("Illegal Operation. Only All Comments GET, Filter, Sort, Allowed.", safe=False)


@csrf_exempt
def like_comment(request, id=0):
    if request.method == "PUT":
        parsed_data = JSONParser().parse(request)
        try:
            comment = models.PostComment.objects.get(CommentId=id)
        except:
            return JsonResponse("Comment you are trying to like does not exist.", safe=False)
        if str(parsed_data.get('LikedById')) in comment.LikedBy:
            return JsonResponse("You cannot like the same comment more than once.", safe=False)
        try:
            liker = models.UserProfile.objects.get(
                ProfileId=parsed_data.get('LikedById'))
            comment.Likes = comment.Likes + 1
            if comment.LikedBy == "":
                comment.LikedBy = parsed_data.get('LikedById')
            else:
                comment.LikedBy = str(comment.LikedBy) + \
                    ";" + str(liker.ProfileId)
            comment.save()
            return JsonResponse("Comment Liked Successfully !!!", safe=False)
        except:
            comment.Likes = comment.Likes + 1
            if comment.LikedBy == "":
                comment.LikedBy = parsed_data.get('LikedById')
            else:
                comment.LikedBy = str(comment.LikedBy) + \
                    ";0"
            comment.save()
            return JsonResponse("LikedById is not a valid user so liking comment anonymously. Comment Liked Successfully !!!", safe=False)
    return JsonResponse("Illegal Operation. Only Like Comment via PUT allowed.", safe=False)


@csrf_exempt
def dislike_comment(request, id=0):
    if request.method == "PUT":
        parsed_data = JSONParser().parse(request)
        try:
            comment = models.PostComment.objects.get(CommentId=id)
        except:
            return JsonResponse("Comment you are trying to dislike does not exist.", safe=False)
        if str(parsed_data.get('DislikedById')) in comment.DislikedBy:
            return JsonResponse("You cannot dislike the same comment more than once.", safe=False)
        try:
            disliker = models.UserProfile.objects.get(
                ProfileId=parsed_data.get('DislikedById'))
            comment.Dislikes = comment.Dislikes + 1
            if comment.DislikedBy == "":
                comment.DislikedBy = parsed_data.get('DislikedById')
            else:
                comment.DislikedBy = str(comment.DislikedBy) + \
                    ";" + str(disliker.ProfileId)
            comment.save()
            return JsonResponse("Comment Disliked Successfully !!!", safe=False)
        except:
            comment.Dislikes = comment.Dislikes + 1
            if comment.DislikedBy == "":
                comment.DislikedBy = parsed_data.get('DislikedById')
            else:
                comment.DislikedBy = str(comment.DislikedBy) + \
                    ";0"
            comment.save()
            return JsonResponse("DislikedById is not a valid user so disliking comment anonymously. Comment Disliked Successfully !!!", safe=False)
    return JsonResponse("Illegal Operation. Only Dislike Comment via PUT allowed.", safe=False)
