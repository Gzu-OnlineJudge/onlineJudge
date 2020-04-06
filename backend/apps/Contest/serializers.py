from rest_framework import serializers

from .models import *
from Issue.models import *


class MatchSerializer(serializers.ModelSerializer):
    reg_status = serializers.IntegerField(default=0)
    ownerName = serializers.CharField(source="owner.username")
    ownerNickname = serializers.CharField(source="owner.nickname")

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
    matchName = serializers.CharField(source="match.matchName", default="")
    proNo = serializers.IntegerField(source="problem.no", default="")
    title = serializers.CharField(source="problem.title", default="")
    classification = serializers.CharField(source="problem.classification", default="")
    probAuthority = serializers.CharField(source="problem.probAuthority", default="")

    class Meta:
        model = MatchInclude
        fields = ("ac_num", "total_num", "matchName", "proNo", "title", "classification", "probAuthority")


class MatchRankSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(source="user.username")
    userNickname = serializers.CharField(source="user.nickname")
    userId = serializers.IntegerField(source="user.id")
    userSchool = serializers.CharField(source="user.school")

    class Meta:
        model = MatchRank
        fields = ("userName", "userNickname", "userId", "userSchool", "acnum", "rank")
