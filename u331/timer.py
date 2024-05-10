import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def usage(self):
        print("\n----------- STOPWATCH -----------")
        print("|-> s      : start the stopwatch |")


    def start(self):
        self.start_time = time.time()

    def start_countdown(self, seconds_countdown=3):
        user_input = input("\n-> Press 's' when you're ready to start: ")
        while seconds_countdown > 0:
            print(f"\rStarting in {seconds_countdown}...", end="")
            time.sleep(1)
            seconds_countdown -= 1
        print("\rGO !", end="")

    def stop(self):
        self.end_time = time.time()
        print(f"\n\nTotal elapsed time: {(self.end_time - self.start_time):.3f} seconds\n")
        exit(0)

    def run(self):
        self.usage()
        self.start_countdown()
        self.start()
        try:
            while True:
                print(f"\rElapsed time: {(time.time() - self.start_time):.0f} seconds", end="")
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.run()