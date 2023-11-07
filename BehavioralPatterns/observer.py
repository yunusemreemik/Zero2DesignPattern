# Step 1: Subject (Observable)
class NewsAgency:
    def __init__(self):
        self._subscribers = []

    def add_subscriber(self, subscriber):
        self._subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self, news):
        for subscriber in self._subscribers:
            subscriber.update(news)

# Step 2: Observer (Subscriber)
class NewsSubscriber:
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"{self.name} received news: {news}")

# Step 3: Client Usage
agency = NewsAgency()

subscriber1 = NewsSubscriber("Subscriber 1")
subscriber2 = NewsSubscriber("Subscriber 2")
subscriber3 = NewsSubscriber("Subscriber 3")

agency.add_subscriber(subscriber1)
agency.add_subscriber(subscriber2)
agency.add_subscriber(subscriber3)

agency.notify_subscribers("Breaking News: Python 4.0 Released!")  
# Output:
# Subscriber 1 received news: Breaking News: Python 4.0 Released!
# Subscriber 2 received news: Breaking News: Python 4.0 Released!
# Subscriber 3 received news: Breaking News: Python 4.0 Released!

agency.remove_subscriber(subscriber2)

agency.notify_subscribers("Important Security Alert: Update Your Systems!")  
# Output:
# Subscriber 1 received news: Important Security Alert: Update Your Systems!
# Subscriber 3 received news: Important Security Alert: Update Your Systems!
