from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.group_name = "chat"
        # Join room group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive_json(self, content, **kwargs):
        # Send message to room group
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat",
                "favicon": content["favicon"],
                "message": content["message"],
            },
        )

    # Receive message from room group
    async def chat(self, event):
        # Send message to WebSocket
        await self.send_json(
            {
                "favicon": event["favicon"],
                "message": event["message"],
            },
        )
