from datetime import datetime, timedelta

from rest_framework import serializers
from apps.util import get_data

from .models import *
from Issue.models import *
from UserProfile.serializers import UserSerializer


class MatchSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    @staticmethod
    def get_owner(obj):
        from UserProfile.serializers import UserSerializer
        dataList = []
        user = obj.owner
        data = get_data(obj=user, serializer=UserSerializer, dataList=dataList)
        return data

    @staticmethod
    def get_status(obj):
        time1 = obj.startTime.replace(tzinfo=None)  # 比赛开始时间
        time2 = datetime.now()  # 当前系统时间
        time3 = time1 + timedelta(minutes=int(obj.howLong))  # 比赛结束时间
        flag_time = 0
        if time1 > time2:  # 比赛未开始
            flag_time = 1
        elif time2 < time3 and time2 > time1:  # 比赛进行中
            flag_time = 2
        elif time2 > time3:  # 比赛已结束
            flag_time = 3
        return flag_time

    class Meta:
        model = Match
        method_fields = ["owner"]
        fields = '__all__'


# class MatchSubmitListSerializer(serializers.ModelSerializer):
#     match_id = serializers.CharField(source="match.id")
#     user = serializers.SerializerMethodField()
#     problem_id = serializers.IntegerField(source="problem.no")
#
#     @staticmethod
#     def get_user(obj):
#         return UserSerializer(obj.user).data
#
#     class Meta:
#         model = MatchSubmit
#         fields = ("match_id", "user", "problem_id", "runID", "result", "time", "memory", "language", "subTime",)


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
        method_fields = ["match", "user", "problem"]
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
        data = get_data(obj=problem, serializer=ProblemSerializer, dataList=dataList)
        return data

    class Meta:
        method_fields = ["match", "problem"]
        model = MatchInclude
        fields = "__all__"
        # fields = ("ac_num", "total_num", "match_id", "problem_id", "no", "title", "classification", "probAuthority")


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
        method_fields = ["match", "user"]
        model = MatchRank
        fields = "__all__"
