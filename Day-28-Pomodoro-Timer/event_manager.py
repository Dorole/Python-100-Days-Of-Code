import logging
from config import EventType


class EventManager:
    def __init__(self):
        self.listeners = {event: [] for event in EventType}

    def subscribe(self, event_type, callback):
        if event_type not in self.listeners:
            logging.warning(f"Attempted to subscribe to an unknown event: {event_type}")
            return
        self.listeners[event_type].append(callback)

    def unsubscribe(self, event_type, callback):
        if event_type in self.listeners:
            self.listeners[event_type].remove(callback)

    def raise_event(self, event_type, state=None):
        for callback in self.listeners.get(event_type, []):
            callback(state)




