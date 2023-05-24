from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model, login
from .serializers import UserSerializer, FriendListSerializer
from .models import User

# app_key = '7d4a55845458a5954269e348d1f652b1'

# Create your views here.
# from rest_framework.views import APIView
# from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
# import requests
# import base64
# import json

# class KakaoLoginView(APIView):
#     def get(self, request):
#         kakao_access_code = request.GET.get('code', None)

#         url = "https://kauth.kakao.com/oauth/token"

#         headers = {'Content-type' : 'application/x-www-form-urlencoded; charset=utf-8'}
        
#         body = {
#             'grant_type' : 'authorization_code',
#             'client_id' : app_key,
#             'redirect_uri' : 'http://127.0.0.1:8000/accounts/kakao',
#             'code' : kakao_access_code
#         }
        
#         token_kakao_response = requests.post(url, headers = headers, data = body)

#         response_data = token_kakao_response.json()
#         id_token = response_data['id_token']
#         payload = id_token.split('.')[1]  # JWT의 페이로드 부분 추출
#         decoded_payload = base64.b64decode(payload + '==')  # base64 디코딩
#         kakao_profile = json.loads(decoded_payload)
        
#         access_token = json.loads(token_kakao_response.text).get('access_token')

#         url = 'https://kapi.kakao.com/v2/user/me'
#         headers = {
#             'Authorization': f'Bearer {access_token}',
#             'Content-type' : 'application/x-www-form-urlencoded; charset=utf-8'
#         }

#         kakao_response = requests.get(url, headers=headers)
#         kakao_response = json.loads(kakao_response.text)
        


#         if User.objects.filter(id = kakao_response['id']).exists():
#             user = User.objects.get(id = kakao_response['id'])
#             return HttpResponse(f'id:{user.id}, name:{user.username}, token: {access_token}')

#         User(
#             id = kakao_response['id'],
#             username = kakao_profile['nickname'],
#             email = kakao_profile['email']
#         ).save()

#         user = User.objects.get(id=kakao_response['id'])

#         return HttpResponse(f'id:{user.id}, name:{user.username}, token: {access_token}')



        # # 카카오 응답에서 필요한 정보 추출
        # if 'nickname' in kakao_profile:
        #     username = kakao_profile['nickname']
        # else:
        #     username = kakao_profile['email'].split('@')[0]
        
        # access_token = response_data['access_token']
        # email = kakao_profile['email']
        
        # profile = ''
        # if 'picture' in kakao_profile:
        #     profile = kakao_profile['picture']

        # # 회원 가입 로직 구현
        # user, created = User.objects.get_or_create(username=username, email=email, profile=profile)
        # print(user)
        # # 추가 필요한 정보 저장
        # user.profile.access_token = access_token
        # user.save()

        # # JWT 로그인 처리
        # jwt_payload = {'username': username, 'email': email}
        # response = requests.post('http://127.0.0.1:8000/auth/login/', data=jwt_payload)

        # if response.status_code == 200:
        #     # 로그인 성공 시 리다이렉션
        #     login(request, user)
        #     return redirect('http://localhost:8080/home')  # Vue 화면으로 리다이렉션
        # else:
        #     # 로그인 실패 시 처리
        #     return Response({'message': '로그인에 실패했습니다.'}, status=response.status_code)


@api_view(['GET'])
def findUsername(request):
    print(request.query_params)
    if request.method == "GET":
        user = User.objects.filter(email=request.query_params.get('email'))
        if user:
            serializer = UserSerializer(user[0])
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT'])
def findPw(request):
    user = User.objects.filter(Q(email=request.query_params.get('email')) & Q(username = request.query_params.get('username')))
    if request.method == "GET":
        if user:
            serializer = UserSerializer(user[0])
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == "PUT":
        user[0].set_password(request.data.get('password1'))
        user[0].save()
        return Response({'message': '비밀번호가 성공적으로 변경되었습니다.'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUser(request):
    if request.method == "GET":
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'username' : ''}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def userdelete(request):
    request.user.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request):
    if request.method == "PUT":
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def profile(request,user_pk):
    if request.method=='GET':
        user = get_object_or_404(get_user_model(),pk=user_pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request,user_pk):
    if request.method=='POST':
        user = get_object_or_404(get_user_model(),pk=user_pk)
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def friends(request,user_pk):
    user = get_object_or_404(get_user_model(),pk=user_pk)
    if request.method=='GET':
        serializer = FriendListSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def setscore(request):
    user = request.user
    if request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getChoRank(request):
    # cho_points를 기준으로 내림차순 정렬 후 상위 10개만 가져옴
    choRank = User.objects.all().order_by('-cho_points')[:10]

    if request.method == 'GET':
        serializer = UserSerializer(choRank, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOverviewRank(request):
    # cho_points를 기준으로 내림차순 정렬 후 상위 10개만 가져옴
    overRank = User.objects.all().order_by('-overview_points')[:10]

    if request.method == 'GET':
        serializer = UserSerializer(overRank, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getmyrank(request, game):
    user = request.user

    if game == 'cho_points':
        my_rank = User.objects.filter(cho_points__gt=user.cho_points).count() + 1
    elif game == 'overview_points':
        my_rank = User.objects.filter(overview_points__gt=user.overview_points).count() + 1
    else:
        return Response({"error": "Invalid game"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"rank": my_rank}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getrank(request, game, user_pk):
    user = User.objects.get(pk=user_pk)

    if game == 'cho_points':
        rank = User.objects.filter(cho_points__gt=user.cho_points).count() + 1
    elif game == 'overview_points':
        rank = User.objects.filter(overview_points__gt=user.overview_points).count() + 1
    else:
        return Response({"error": "Invalid game"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"rank": rank}, status=status.HTTP_200_OK)