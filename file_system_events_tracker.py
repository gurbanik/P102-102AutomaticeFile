import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

fromdir = "C:/Users/gurje/Downloads"
todir = "C:/Users/gurje/Desktop/Downloads"

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey {event.src_path}has been created")
    def on_deleted(self, event):
        print(f"Oops, somebody has deleted" {event.src_path})
    def on_modified(self, event):
        print(f"Somebody has modified" {event.src_path})
    def on_moved(self, event):
        print(f"Oops, somebody has moved or renamed" {event.src_path})

eventhandler = FileMovementHandler()
observer = Observer()
observer.schedule(eventhandler, fromdir, recusive = True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()
