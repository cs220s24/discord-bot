import redis
import random

class RedisHandler:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_client = redis.StrictRedis(host=host, port=port, db=db)

    def set_motivational_quotes(self, quotes):
        """Set the motivational quotes in the Redis database."""
        for index, quote in enumerate(quotes):
            self.redis_client.set(f'motivational_quote:{index}', quote)

    def get_random_quote(self):
        """Retrieve a random motivational quote from the Redis database."""
        keys = self.redis_client.keys('motivational_quote:*')
        if keys:
            random_key = random.choice(keys)
            return self.redis_client.get(random_key).decode('utf-8')
        else:
            return "Sorry, no motivational quotes available at the moment."
