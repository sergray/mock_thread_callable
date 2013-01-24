import threading
import mock

from thread_func import func, hello

# without a mock.patch we would see Goodbye
with mock.patch('thread_func.hello', hello) as ctx:
    thread = threading.Thread(target=func)
    thread.start()
    thread.join()
