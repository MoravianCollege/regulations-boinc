import redis
import threading



class RedisManager:

    def __init__(self, commands):
        self.r = redis.Redis()
        self.lock = threading.RLock()


    def add_data(self, job_id, job_units):
        with self.lock:
            self.r.set(job_id, job_units)

    def get_job_units(self, job_id):
            return self.r.get(job_id)

    def delete_all(self):
        self.r.flushall()

    def get_job_id_list(self):
        return self.r.keys()

