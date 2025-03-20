import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone
from .models import CourseChat
from asgiref.sync import sync_to_async
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = f'chat_{self.id}'
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        # Send saved messages to the user
        await self.send_saved_messages()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        # Save the message to the database
        await self.save_chat_message(self.user, self.id, message)
        
        # Send the message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.user.username,
                'datetime': timezone.now().isoformat(),
            }
        )

    @sync_to_async
    def save_chat_message(self, user, course_id, message):
        # Получаем объект CourseChat для указанного курса
        course_chat, created = CourseChat.objects.get_or_create(course_id=course_id)
        # Обновляем сообщения курса, добавляя новое сообщение
        course_chat.messages += f"\n{timezone.now()} - {user.username}: {message}"
        # Сохраняем изменения в базе данных
        course_chat.save()
        
    async def send_saved_messages(self):
        try:
            # Получаем объект CourseChat для указанного курса
            course_chat = await sync_to_async(CourseChat.objects.get)(course_id=self.id)
            # Разбиваем сохраненные сообщения на отдельные строки
            messages = course_chat.messages.split('\n')
            for message in messages:
                # Разделяем строку сообщения на имя пользователя и текст сообщения
                parts = message.split(': ')
                if len(parts) >= 2:
                    parts_date_name = parts[0].split(' - ')
                    username = parts_date_name[-1]
                    content = ': '.join(parts[1:])
                    # Отправляем каждое сохраненное сообщение клиенту через WebSocket
                    await self.send(text_data=json.dumps({
                        'type': 'chat_message',
                        'user': username.strip(),  # Убираем лишние пробелы в имени пользователя
                        'message': content,
                        'datetime': parts_date_name[0:-1],  
                    }))
        except ObjectDoesNotExist:
            # Если объект CourseChat не найден, просто не отправляем сохраненные сообщения
            pass


    # receive message from room group
    async def chat_message(self, event):
        # send message to WebSocket
        await self.send(text_data=json.dumps(event))

