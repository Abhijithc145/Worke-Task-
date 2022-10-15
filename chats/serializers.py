from rest_framework import serializers
from .models import *



class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = "__all__"        

# class create_organization_Serializer(serializers.ModelSerializer):

#     class Meta:
#         model = Organizations
#         fields = "__all__"   

class DepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Department
        fields = "__all__" 
                      
    # organization = organization_Serializer(read_only=True)


class AgentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Agent
        fields = "__all__"     


class BotSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bot
        fields = "__all__"          

class ChannelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Channel
        fields = "__all__"   

class ConversationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Conversations
        fields = "__all__"           

class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = "__all__"                   

class UserprofileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = "__all__"                           