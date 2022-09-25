import json
from channels.generic.websocket import WebsocketConsumer

from accounts.models import TotalUsers_realtime

class ChatConsumer(WebsocketConsumer):
    def connect(self, *args, **kwargs,):
        print('client connected')
        self.accept()

        self.send(text_data=json.dumps({
                'type' : 'connection_established',
                'message': 'You are now connected!'
        }))

        # print(args)
        # print(kwargs)

        # print(self.scope)
        user = self.scope["user"]
        print(user.id, user)

        

        # text_data_json = json.loads(text_data)
        # message = text_data_json['user_ip']
        # print('ip is : ', message)

        # sending response back to client(html page)
        # self.send(text_data=json.dumps({
        #     'type':'chat',
        #     'message':message
        # }))

    def receive(self, text_data):

        # print(text_data, 'text_data')
        # text_data_json = json.loads(text_data)
        # message = text_data_json['user_ip']
        # print('ip is : ', message)
        
        
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('Message : ', message, type(message))

        # self.send(text_data=json.dumps({
        #     'type':'chat',
        #     'message':message
        # }))

        self.scope['ip_address'] = message # session setting

        if not TotalUsers_realtime.objects.filter(ip_address=message).exists():
            TotalUsers_realtime.objects.create(ip_address=message)
            print('New(Anonymous) user connected and ip_address created once - receive')
            
        else:
            print('User ip_address already exist - receive')

        total_users = TotalUsers_realtime.objects.all().count()
        print('total_users - ', total_users)




    def disconnect(self, code):
        print('client disconnected')

        try:
            ip_address = self.scope['ip_address']
            print(ip_address)
            if TotalUsers_realtime.objects.filter(ip_address=ip_address).exists():
                db = TotalUsers_realtime.objects.get(ip_address=ip_address)
                db.delete()
                print('Anonymous user ip_address founded and deleted succefully - disconnect')
            else:
                print('Anonymous User ip_address not exist - disconnect')

        except :
            print('abhi this is exception error - disconnect')

        total_users = TotalUsers_realtime.objects.all().count()
        print('total_users - ', total_users)
