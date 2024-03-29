"""
영상 프레임 통신을 위한 모듈
"""
import socket
import cv2
import struct

# 서버 설정
host = "127.0.0.1"
port = 2000


class SendFrame:
    """영상 프레임 통신을 위한 클래스 (HW -> Server)"""
    def __init__(self):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

    def __del__(self):
        self.client_socket.close()

    def send_frame(self, frame):
        _, img_encode = cv2.imencode('.jpg', frame)
        img_bytes = img_encode.tobytes()
        
        self.client_socket.sendall(struct.pack("!I", len(img_bytes)))
        
        self.client_socket.sendall(img_bytes)