import capnp
import zmq

capnp.remove_import_hook()
fh_capnp = capnp.load('../../../../serenity-fh/capnp/serenity-fh.capnp')

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect("tcp://localhost:5556")
socket.setsockopt_string(zmq.SUBSCRIBE, "")

while True:
    msg_bytes = socket.recv()
    msg = fh_capnp.TradeMessage.from_bytes(msg_bytes)
    print("{} {} @ {}".format(msg.side, msg.size, msg.price))
