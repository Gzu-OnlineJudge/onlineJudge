from datetime import datetime

from rest_framework import serializers
from apps.util import get_data

from .models import *


class MatchSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    @staticmethod
    def get_owner(obj):
        from UserProfile.serializers import UserSerializer
        dataList = []
        user = obj.owner
        data = get_data(obj=user, serializer=UserSerializer, dataList=dataList)
        return data

    class Meta:
        model = Match
        fields = '__all__'


class MatchSubmitSerializer(serializers.ModelSerializer):
    match = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    problem = serializers.SerializerMethodField()

    @staticmethod
    def get_match(obj):
        dataList = ["id"]
        match = obj.match
        data = get_data(obj=match, serializer=MatchSerializer, dataList=dataList)
        return data

    @staticmethod
    def get_user(obj):
        from UserProfile.serializers import UserSerializer
        dataList = []
        user = obj.user
        data = get_data(obj=user, serializer=UserSerializer, dataList=dataList)
        return data

    @staticmethod
    def get_problem(obj):
        from Issue.serializers import ProblemSerializer
        dataList = ["no", "title"]
        problem = obj.user
        data = get_data(obj=problem, serializer=ProblemSerializer, dataList=dataList)
        return data

    class Meta:
        model = MatchSubmit
        fields = '__all__'


class MatchRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchRegister
        fields = '__all__'


class MatchIncludeSerializer(serializers.ModelSerializer):
    match = serializers.SerializerMethodField()
    problem = serializers.SerializerMethodField()

    @staticmethod
    def get_match(obj):
        dataList = ["id"]
        match = obj.match
        data = get_data(obj=match, serializer=MatchSerializer, dataList=dataList)
        return data

    @staticmethod
    def get_problem(obj):
        from Issue.serializers import ProblemSerializer
        dataList = ["no", "title", "classification", "probAuthority"]
        problem = obj.user
        data = get_data(obj=problem, serializer=ProblemSerializer, dataList='__all__')
        return data

    class Meta:
        model = MatchInclude
        fields = "__all__"


class MatchRankSerializer(serializers.ModelSerializer):
    match = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    @staticmethod
    def get_match(obj):
        dataList = ["id"]
        match = obj.match
        data = get_data(obj=match, serializer=MatchSerializer, dataList=dataList)
        return data

    @staticmethod
    def get_user(obj):
        from UserProfile.serializers import UserSerializer
        dataList = ["id", "username", "nickname", "school"]
        user = obj.user
        data = get_data(obj=user, serializer=UserSerializer, dataList=dataList)
        return data

    class Meta:
        model = MatchRank
        fields = "__all__"
