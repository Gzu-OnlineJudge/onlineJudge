from rest_framework import serializers

from .models import *
from Issue.models import *


class MatchSerializer(serializers.ModelSerializer):

    reg_status = serializers.IntegerField(default=0)
    owner = serializers.SerializerMethodField()

    @staticmethod
    def get_owner(obj):
        from UserProfile.serializers import UserSerializer
        data = UserSerializer(obj.owner).data
        return data

    class Meta:
        model = Match
        fields = '__all__'


class MatchSubmitListSerializer(serializers.ModelSerializer):
    matchId = serializers.CharField(source="match.id")
    userName = serializers.CharField(source="user.username")
    userId = serializers.IntegerField(source="user.id")
    probId = serializers.IntegerField(source="problem.no")
    probName = serializers.CharField(source="problem.title")

    class Meta:
        model = MatchSubmit
        fields = ("matchId", "userName", "userId", "probId", "probName",
                  "runID", "result", "time", "memory", "language", "subTime",)


class MatchSubmitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MatchSubmit
        fields = '__all__'


class MatchRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = MatchRegister
        fields = '__all__'


class MatchIncludeSerializer(serializers.ModelSerializer):
    match_id = serializers.IntegerField(source="match.id", default=0)
    problem_id = serializers.IntegerField(source="problem.no", default=1000)
    title = serializers.CharField(source="problem.title", default="")
    classification = serializers.CharField(source="problem.classification", default="")
    probAuthority = serializers.CharField(source="problem.probAuthority", default="")

    class Meta:
        model = MatchInclude
        fields = ("ac_num", "total_num", "match_id", "problem_id", "no", "title", "classification", "probAuthority")


class MatchRankSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(source="user.username")
    userNickname = serializers.CharField(source="user.nickname")
    userId = serializers.IntegerField(source="user.id")
    userSchool = serializers.CharField(source="user.school")

    class Meta:
        model = MatchRank
        fields = ("userName", "userNickname", "userId", "userSchool", "acnum", "rank")
