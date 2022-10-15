from django.urls import path,include
from .import views
from .views import *
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path("organizations/",OrganizationsList.as_view(),name="chat_organizations"),
    path("organizations/<uuid:pk>",organizationDetails.as_view(),name="chat_organizationslist"),
    path("bots/",BotList.as_view(),name="bots"),
    path("bots/<uuid:pk>/organization/<uuid:org>",BotDetails.as_view(),name="bots_data"),
    path("departments/",DepartmentList.as_view(),name="department_data"),
    path("departments/<uuid:pk>/organization/<uuid:org>/bot/<uuid:bot>",DepartmentDetails.as_view(),name="department_data"),
    path("agents/",AgentList.as_view(),name="agents"),
    path("agents/<uuid:pk>",AgentDetails.as_view(),name="agents_data"),
    path("conversations/",ConversationList.as_view(),name="bots"),
    path("conversations/<uuid:pk>",ConversationDetails.as_view(),name="bots_data"),
    path("message/",MessageList.as_view(),name="message_data"),
    path("message/<uuid:pk>",MessageDetails.as_view(),name="bots_data"),
    path("userprofiles/",UserProfileList.as_view(),name="userprofile_data"),
    path("userprofiles/<uuid:pk>",UserProfileDetails.as_view(),name="userprofile_data"),
    path("channels/",ChannelList.as_view(),name="channel_data"),
    path("channels/<uuid:pk>",ChannelDetails.as_view(),name="userprofile_data"),

    
]



