# python3
import datetime
from collections import namedtuple
import logging

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.INFO)
logging.Logger.disabled = True


Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.buffer = 0
        self.pending_get = []

    def process(self, request):
        st = datetime.datetime.now()
        logging.info("pending_get is :%d" % len(self.pending_get))
        if len(self.pending_get) > 0:
            while self.pending_get[0] <= request.arrived_at:
                if self.buffer - 1 >= 0:
                    self.buffer -= 1
                self.pending_get.pop(0)
                break
        logging.info("process mid %s" % (datetime.datetime.now() - st))
        if self.buffer + 1 <= self.size:
            self.buffer += 1
            start_time = 0
            if len(self.pending_get) > 0:
                start_time = self.pending_get[-1]
            start_time = max(request.arrived_at, start_time)
            self.pending_get.append(start_time + request.time_to_process)
            logging.info("process %s" % (datetime.datetime.now() - st))
            return Response(False, start_time)
        logging.info("process %s" % (datetime.datetime.now() - st))
        return Response(True, -1)


def process_requests(requests, buffer):

    responses = []
    st1 = datetime.datetime.now()
    for request in requests:
        st = datetime.datetime.now()
        res = buffer.process(request)
        # logging.info("get res : %s" % (datetime.datetime.now() - st))
        responses.append(res)
        # logging.info("appended : %s" % (datetime.datetime.now() - st))
    logging.info("total time is %s" % (datetime.datetime.now() - st1))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
