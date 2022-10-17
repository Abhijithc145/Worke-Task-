from django.urls import path,include
from .import views
from .views import *
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path("organizations/",OrganizationsList.as_view(),name="chat_organizations"),
    path("organizations/<uuid:pk>",organizationDetails.as_view(),name="chat_organizationslist"),

    path("organizations/<uuid:org>/bots/",BotList.as_view(),name="bots"),
    # path("organization/bots/",BotList.as_view(),name="bots"),
    path("organizations/<uuid:org>/bots/<uuid:pk>",BotDetails.as_view(),name="bots_data"),

    path("organizations/<uuid:org>/departments/",DepartmentList.as_view(),name="department_data"),
    path("organizations/<uuid:org>/departments/<uuid:pk>",DepartmentDetails.as_view(),name="department_data"),

    path("organizations/<uuid:org>/departments/<uuid:dep>/agents/",AgentList.as_view(),name="agents"),
    path("organizations/<uuid:org>/departments/<uuid:dep>/agents/<uuid:pk>",AgentDetails.as_view(),name="agents_data"),

    path("bots/<uuid:bot>/conversations/",ConversationList.as_view(),name="bots"),
    path("bots/<uuid:bot>/conversations/<uuid:pk>",ConversationDetails.as_view(),name="bots_data"),

    path("organizations/<uuid:org>/conversations/<uuid:conv>/messages/",MessageList.as_view(),name="message_data"),
    path("organizations/<uuid:org>/conversations/<uuid:conv>/messages/<uuid:pk>",MessageDetails.as_view(),name="bots_data"),

    path("organizations/<uuid:org>/bots/<uuid:bot>/userprofiles/",UserProfileList.as_view(),name="userprofile_data"),
    path("organizations/<uuid:org>/bots/<uuid:bot>/userprofiles/<uuid:pk>",UserProfileDetails.as_view(),name="userprofile_data"),

    path("organizations/<uuid:org>/bots/<uuid:bot>/channels/",ChannelList.as_view(),name="channel_data"),
    path("organizations/<uuid:org>/bots/<uuid:bot>/channels/<uuid:pk>",ChannelDetails.as_view(),name="userprofile_data"),

]



