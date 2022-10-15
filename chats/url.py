from django.urls import path,include
from .import views
from .views import *
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path("organizations/",OrganizationsList.as_view(),name="chat_organizations"),
    path("organizations/<uuid:pk>",organizationDetails.as_view(),name="chat_organizationslist"),

    path("organization/<uuid:org>/bots/",BotList.as_view(),name="bots"),
    # path("organization/bots/",BotList.as_view(),name="bots"),
    path("organization/bots/<uuid:pk>",BotDetails.as_view(),name="bots_data"),

    path("organization/departments/",DepartmentList.as_view(),name="department_data"),
    path("organization/departments/<uuid:pk>",DepartmentDetails.as_view(),name="department_data"),

    path("organization/departments/agents/",AgentList.as_view(),name="agents"),
    path("organization/departments/agents/<uuid:dep>",AgentDetails.as_view(),name="agents_data"),

    path("organization/bots/conversations/",ConversationList.as_view(),name="bots"),
    path("organization/bots/conversations/<uuid:pk>",ConversationDetails.as_view(),name="bots_data"),

    path("organization/bots/conversations/message/",MessageList.as_view(),name="message_data"),
    path("message/<uuid:pk>/conversation/<uuid:conv>",MessageDetails.as_view(),name="bots_data"),

    path("organization/bots/userprofiles/",UserProfileList.as_view(),name="userprofile_data"),
    path("organization/bots/userprofiles/<uuid:pk>",UserProfileDetails.as_view(),name="userprofile_data"),

    path("organization/bots/channels/",ChannelList.as_view(),name="channel_data"),
    path("organization/bots/channels/<uuid:pk>",ChannelDetails.as_view(),name="userprofile_data"),

]



