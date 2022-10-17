from telnetlib import STATUS
from xml.dom import ValidationErr
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from .models import *
from django.shortcuts import render,get_object_or_404
import datetime
from rest_framework import viewsets
# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


# organization CRUD

class OrganizationsList(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Organization.objects.filter(is_active = True)
    serializer_class = OrganizationSerializer
    def get(self,request,*args,**kwargs):
        
        return self.list(request,*args,**kwargs)  

    def post(self,request,*args,**kwargs):
        
        return self.create(request,*args,**kwargs) 


class organizationDetails(APIView):
    def get(self,request,pk = None):

        if pk:
            try:
                datas = Organization.objects.get(id=pk,is_active = True)
                serializer = OrganizationSerializer(datas)
                return Response({ "data": serializer.data}, status=status.HTTP_200_OK)
            except:
                return Response({"Error":"The data is no here"})    
 
        datas = Organization.objects.all()
        serializer = OrganizationSerializer(datas, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)  


    def put(self,request,pk = None):
        try:
            datas = Organization.objects.get(id=pk)
            serializer = OrganizationSerializer(datas, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors})   
        except:
                return Response({"Error":"The data is no here"})          

    def delete(self,request,pk = None):
        data = get_object_or_404(Organization, id = pk)
        data.is_active = not(data.is_active)
        data.deleted_at =datetime.datetime.now() 
        data.save()
        return Response({"status": "success", "data": "student Deleted"})                    



#       Department CRUD

class DepartmentList(APIView):
    def get(self,request,org):
        print(org)
        datas = Department.objects.filter(is_active = True)
        serializer =DepartmentSerializer(datas,many=True)
        return Response(serializer.data)  
        
    def post(self,request,org):
        try:

            print(org)
            serializer = DepartmentSerializerValidation(data=request.data)
            if serializer.is_valid():   
                serializer.save()
                print(serializer)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)    
        except Exception as err:
            print(err)
            return Response("ERR")  



class DepartmentDetails(APIView):
    def get(self,request,pk,org):
        try:
            print(org)
            datas = Department.objects.get(id=pk,is_active = True)
            serilizer = DepartmentSerializer(datas)
            return Response({ "data": serilizer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  

    def put(self,request,pk,org):
        try:
            print(org)
            datas = Department.objects.get(id=pk,is_active = True)
            serializer = DepartmentSerializerValidation(datas, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors}) 
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  


    def delete(self,request,pk,org):
        try:
            print(org)
            data = get_object_or_404(Department, id = pk)
            data.is_active = not(data.is_active)
            data.deleted_at =datetime.datetime.now() 
            data.save()
            return Response({"status": "success", "data": "student Deleted"}) 
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  
        



class AgentList(APIView):
    def get(self,request,org,dep):
        datas = Agent.objects.filter(is_active = True)
        serializer =AgentSerializer(datas,many=True)
        return Response(serializer.data)  
        
    def post(self,request,org,dep):
        try:
     
            serializer = AgentSerializerValidation(data=request.data)
            if serializer.is_valid():   
                serializer.save()
                print(serializer)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)    
        except Exception as err:
            print(err)
            return Response("ERR")  


class AgentDetails(APIView):   
    def get(self,request,pk,org,dep):
        try:
            datas = Agent.objects.get(id=pk,is_active = True)
            serilizer = AgentSerializer(datas)
            return Response({ "data": serilizer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  

    def put(self,request,pk,org,dep):
        try:
            datas = Agent.objects.get(id=pk,is_active = True)
            serializer = AgentSerializerValidation(datas, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors}) 
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  


    def delete(self,request,pk,org,dep):
        try:
            data = get_object_or_404(Agent, id = pk)
            data.is_active = not(data.is_active)
            data.deleted_at =datetime.datetime.now() 
            data.save()
            return Response({"status": "success", "data": "student Deleted"}) 
        except Exception as err:
            print(err)         



class BotList(APIView):
    def get(self,request,org):
        print(org)
        datas = Bot.objects.filter(is_active = True)
        serializer =BotSerializer(datas,many=True)
        return Response(serializer.data)  
        
    def post(self,request,org):
        try:
            print(org)
            serializer = BotSerializerValidation(data=request.data)
            value = request.data.copy()
            print(value["organization"])
            
            if serializer.is_valid():   
                serializer.save()
                print(serializer)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)    
        except Exception as err:
            print(err)
            return Response("ERR")              


class BotDetails(APIView):   
    def get(self,request,pk,org):
        try:
            print(org)
            datas = Bot.objects.get(id=pk,is_active = True)
            serilizer = BotSerializer(datas).data
            
            return Response({ "data": serilizer}, status=status.HTTP_200_OK)
            
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  

    def put(self,request,pk,org):
        try:
            print(org)
            datas = Bot.objects.get(id=pk,is_active = True)
            serializer = BotSerializerValidation(datas, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors}) 
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  


    def delete(self,request,pk):
        try:
            data = get_object_or_404(Bot, id = pk)
            data.is_active = not(data.is_active)
            data.deleted_at =datetime.datetime.now() 
            data.save()
            return Response({"status": "success", "data": "student Deleted"}) 
        except Exception as err:
            print(err)         

class ConversationList(APIView):
    def get(self,request,bot):
        datas = Conversations.objects.filter(is_active = True)
        serializer =ConversationSerializer(datas,many=True)
        return Response(serializer.data)  
        
    def post(self,request,bot):
        data=request.data
        try:
            try:
                userprofile = UserProfile.objects.get(sender_id=data['sender_id'],bot=bot)
            except UserProfile.DoesNotExist:
                userprofile.objects.create(data=data)
            serializer = ConversationSerializerValidation(data=request.data)
            if serializer.is_valid():   
                serializer.save()
                print(serializer)

                return Response(serializer.data)
            else:
                return Response(serializer.errors)    
        except Exception as err:
            print(err)
            return Response("ERR")     


class ConversationDetails(APIView):   
    def get(self,request,pk,bot):
        try:
            datas = Conversations.objects.get(id=pk,is_active = True)
            serilizer = ConversationSerializer(datas)
            return Response({ "data": serilizer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  

    def put(self,request,pk,bot):
        try:
            datas = Conversations.objects.get(id=pk,is_active = True)
            serializer = ConversationSerializerValidation(datas, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors}) 
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  


    def delete(self,request,pk,bot):
        try:
            data = get_object_or_404(Conversations, id = pk)
            data.is_active = not(data.is_active)
            data.deleted_at =datetime.datetime.now() 
            data.save()
            return Response({"status": "success", "data": "student Deleted"}) 
        except Exception as err:
            print(err)  


class MessageList(APIView):
    def get(self,request,org,conv):
        datas =Message.objects.filter(is_active = True)
        serializer =MessageSerializer(datas,many=True)
        return Response(serializer.data)  
        
    def post(self,request,org,conv):
        print(request.data,";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        try:
     
            serializer = MessageSerializerValidation(data=request.data)
            if serializer.is_valid():   
                serializer.save()
                print(serializer)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)    
        except Exception as err:
            print(err)
            return Response("ERR")     


class MessageDetails(APIView):   
    def get(self,request,pk,org,conv):
        try:
            datas = Message.objects.get(id=pk,is_active = True)
            serilizer = MessageSerializer(datas)
            return Response({ "data": serilizer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  

    def put(self,request,pk,org,conv):
        try:
            datas = Message.objects.get(id=pk,is_active = True)
            serializer = MessageSerializerValidation(datas, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors}) 
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  


    def delete(self,request,pk,org,conv):
        try:
            data = get_object_or_404(Message, id = pk)
            data.is_active = not(data.is_active)
            data.deleted_at =datetime.datetime.now() 
            data.save()
            return Response({"status": "success", "data": "student Deleted"}) 
        except Exception as err:
            print(err)  


class UserProfileList(APIView):
    def get(self,request,org,bot):
        datas =UserProfile.objects.filter(is_active = True)
        serializer =UserprofileSerializer(datas,many=True)
        return Response(serializer.data)  
        
    def post(self,request,org,bot):
        print(request.data,";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        try:
     
            serializer = UserprofileSerializerValidation(data=request.data)
            if serializer.is_valid():   
                serializer.save()
                print(serializer)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)    
        except Exception as err:
            print(err)
            return Response("ERR")   




class UserProfileDetails(APIView):   
    def get(self,request,pk,org,bot):
        try:
            datas = UserProfile.objects.get(id=pk,is_active = True)
            serilizer = UserprofileSerializer(datas)
            return Response({ "data": serilizer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  

    def put(self,request,pk,org,bot):
        try:
            datas = UserProfile.objects.get(id=pk,is_active = True)
            serializer = UserprofileSerializer(datas, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors}) 
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  


    def delete(self,request,pk,bot,org):
        try:
            data = get_object_or_404(UserProfile, id = pk)
            data.is_active = not(data.is_active)
            data.deleted_at =datetime.datetime.now() 
            data.save()
            return Response({"status": "success", "data": "student Deleted"}) 
        except Exception as err:
            print(err)  

            


class ChannelList(APIView):
    def get(self,request,org,bot):
        datas =Channel.objects.filter(is_active = True)
        serializer =ChannelSerializer(datas,many=True)
        return Response(serializer.data)  
        
    def post(self,request,org,bot):
        print(request.data,";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        try:
     
            serializer = ChannelSerializerValidation(data=request.data)
            if serializer.is_valid():   
                serializer.save()
                print(serializer)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)    
        except Exception as err:
            print(err)
            return Response("ERR")            


#             

class ChannelDetails(APIView):   
    def get(self,request,pk,org,bot):
        try:
            datas = Channel.objects.get(id=pk,is_active = True)
            serilizer = ChannelSerializer(datas)
            return Response({ "data": serilizer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  

    def put(self,request,pk,org,bot):
        try:
            datas = Channel.objects.get(id=pk,is_active = True)
            serializer = ChannelSerializerValidation(datas, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors}) 
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  


    def delete(self,request,pk,org,bot):
        try:
            data = get_object_or_404(Channel, id = pk)
            data.is_active = not(data.is_active)
            data.deleted_at =datetime.datetime.now() 
            data.save()
            return Response({"status": "success", "data": "student Deleted"}) 
        except Exception as err:
            print(err)  

