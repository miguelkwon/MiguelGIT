import socket
import pandas as pd

def save_to_excel(data, filename='received_data.xlsx'):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f'Data saved to {filename}')

def start_server(host='0.0.0.0', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f'Server started at {host}:{port}')
        
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)
            if data:
                received_data = eval(data.decode())  # eval은 보안상 위험할 수 있으니, 안전한 형태로 데이터를 전송하는 것이 좋습니다
                save_to_excel(received_data)

if __name__ == "__main__":
    start_server()
