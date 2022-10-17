from asyncore import read
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

class BotSerializer(serializers.ModelSerializer):
    
    organization = OrganizationSerializer(read_only =True)
    class Meta:
        model = Bot
        fields = "__all__"          


class BotSerializerValidation(serializers.ModelSerializer):
    
    class Meta:
        model = Bot
        fields = "__all__"  


class DepartmentSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only = True)
    bot = BotSerializer(read_only = True)

    class Meta:
        model = Department
        fields = "__all__" 

class DepartmentSerializerValidation(serializers.ModelSerializer):
    
    class Meta:
        model = Department
        fields = "__all__"         
                      
    # organization = organization_Serializer(read_only=True)


class AgentSerializer(serializers.ModelSerializer):
    department=DepartmentSerializer(read_only = True)
    class Meta:
        model = Agent
        fields = "__all__"     




class AgentSerializerValidation(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = "__all__"     




class ChannelSerializer(serializers.ModelSerializer):
    bot = BotSerializer(read_only = True)
    class Meta:
        model = Channel
        fields = "__all__"   


class ChannelSerializerValidation(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__" 


class ConversationSerializer(serializers.ModelSerializer):
    bot = BotSerializer(read_only = True)
    agent = AgentSerializer(read_only = True)

    class Meta:
        model = Conversations
        fields = "__all__"      

class ConversationSerializerValidation(serializers.ModelSerializer):
    
    class Meta:
        model = Conversations
        fields = "__all__"   


class MessageSerializer(serializers.ModelSerializer):
    conversation = ConversationSerializer()
    
    class Meta:
        model = Message
        fields = "__all__"                  

class MessageSerializerValidation(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = "__all__"   


class UserprofileSerializer(serializers.ModelSerializer):
    bot = BotSerializer(read_only = True)
    
    class Meta:
        model = UserProfile
        fields = "__all__"     

class UserprofileSerializerValidation(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"                                   