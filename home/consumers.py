from channels.consumer import SyncConsumer , AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync


class myasyncconsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("websocket connected successfully...",event)
        print("Channel layer", self.channel_layer)
        print("Channel name", self.channel_name)
        await self.channel_layer.group_add('workers',self.channel_name)
        await self.send({
           'type':'websocket.accept',
        })
    async def websocket_receive(self,event):
     print("received successfully...")
     print("message is :" , event['text'])
     await self.channel_layer.group_send('workers',{
        'type':'chat.message',
        'message':event['text'],
     })
   
    async def chat_message(self,event):
       print("event", event)
       event_str = str(event)
       await self.send({
          'type':'websocket.send',
          'text':event['message']
       })
    async def websocket_disconnect(self,event):
     print("websocket disconnect successfully...")
     self.channel_layer.group_discard('workers',self.channel_name)
     raise StopConsumer()


class mysyncconsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("websocket connected successfully...",event)
        self.send({
           'type':'websocket.accept',
        })
    def websocket_receive(self,event):
     print("received successfully...")
     print("message is :" , event['text'])
     self.send({
        'type':'websocket.send',
         'text':'we got your message',
     })
    def websocket_disconnect(self,event):
     print("websocket disconnect successfully...")
     raise StopConsumer()