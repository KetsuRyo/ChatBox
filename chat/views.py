from django.shortcuts import render
from rest_framework.decorators import api_view
import openai

from rest_framework.response import Response
from rest_framework import viewsets

from .models import Message
from .serializers import MessageSerializer

openai.api_key = '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'

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    def create(self, request, *args, **kwargs):
        # 调用父类的create方法以正常创建消息
        response = super().create(request, *args, **kwargs)
        
        # 获取刚刚创建的消息对象
        message = Message.objects.get(id=response.data['id'])
        
        # 使用OpenAI API获取回答
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message.content},
            ],
            max_tokens=150
        )
        
        # 将回答保存到消息对象的response字段中
        message.response = res['choices'][0]['message']['content'].strip()
        message.save()
        
        return response
@api_view(['POST'])
def clear_chat(request):
    Message.objects.all().delete()  # 删除所有消息
    return Response({"status": "Chat cleared"})

def index(request):
    print("get")
    return render(request, 'chat/index.html')