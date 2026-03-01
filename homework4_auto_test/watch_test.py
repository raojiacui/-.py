# -*- coding: utf-8 -*-
# Homework 4 Watchdog Auto Test Script
# Monitors homework file changes and runs tests automatically

import sys
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Add path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import test module
import test_homework4


class HomeworkFileHandler(FileSystemEventHandler):
    """File change handler"""

    def __init__(self, filename):
        self.filename = filename
        self.last_modified = 0

    def on_modified(self, event):
        """File modification event"""
        # Only process target file
        if not event.is_directory and event.src_path.endswith(self.filename):
            # Prevent duplicate triggers
            current_time = time.time()
            if current_time - self.last_modified < 1:
                return
            self.last_modified = current_time

            print(f"\n[CHANGE] Detected change in {self.filename}, running tests...")
            print("[TIME] " + time.strftime("%Y-%m-%d %H:%M:%S"))

            # Run tests
            try:
                test_homework4.run_all_tests()
            except Exception as e:
                print(f"[ERROR] Test run failed: {e}")


def main():
    """Main function"""
    # Target file path
    target_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_file = '作业四.py'
    target_path = os.path.join(target_dir, target_file)

    print("=" * 60)
    print("[WATCH] Homework 4 Auto Test Monitor")
    print("=" * 60)
    print(f"[DIR] Monitoring: {target_dir}")
    print(f"[FILE] Target: {target_file}")
    print("=" * 60)
    print("[TIP] Tests will run automatically when you save the file")
    print("[TIP] Press Ctrl+C to stop")
    print("=" * 60)

    # Run initial test
    print("\n[INIT] Initial test run:")
    try:
        test_homework4.run_all_tests()
    except Exception as e:
        print(f"[ERROR] Initial test failed: {e}")

    # Create observer
    event_handler = HomeworkFileHandler(target_file)
    observer = Observer()
    observer.schedule(event_handler, target_dir, recursive=False)
    observer.start()

    print("\n[WAIT] Monitoring for file changes...\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n[STOP] Stopping monitor")
        observer.stop()

    observer.join()
    print("[BYE] Goodbye!")


if __name__ == '__main__':
    main()
