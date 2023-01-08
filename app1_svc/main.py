import socketio

connections = {
    's1': 'http://localhost:6000',
    's2': 'http://localhost:8000'
}


class SocketActions:
    @staticmethod
    def on_connect(src):
        def connect():
            print(f'connection {src} established ')

        return connect

    @staticmethod
    def on_connect_error(src):
        return lambda: print(f"The connection {src} failed!")

    @staticmethod
    def on_message(src):
        def message(data):
            print('message received from  with ', data)

        return message

    @staticmethod
    def on_disconnect(src):
        def disconnect():
            print(f'disconnected {src}  from server')
        return disconnect


sio_connections = {}
for key, con in connections.items():
    sio = socketio.Client()
    sio.event(SocketActions.on_connect(con))
    sio.event(SocketActions.on_disconnect(con))
    sio.event(SocketActions.on_connect_error(con))
    sio.event(SocketActions.on_message(con))
    sio.connect(con)
    sio_connections[key] = sio

sio_connections["s1"].emit('message', {'name': 'app2'})
sio_connections["s2"].emit('message', {'name': 'app3'})

#sio_connections["s1"].wait()

