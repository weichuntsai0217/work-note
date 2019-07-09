"""
  Use python 3.6.8
"""
import socket
import concurrent.futures

def main():
  SERVERPORT = 8080
  NTHREADS = 2

  executor = concurrent.futures.ThreadPoolExecutor(max_workers=NTHREADS)
  serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serversock.bind(('', SERVERPORT))
  serversock.listen(5)
  while True:
    sock, addr = serversock.accept()
    executor.submit(process_req, sock)

if __name__ == '__main__':
  main()
