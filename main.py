from keepalive import KeepAlive
from time import sleep


def run():
    # clear the screen before running the script
    print("\033[H\033[J")
    email = input("Enter your email: ")
    print("\033[H\033[J")
    password = input("Enter your password: ")
    print("\033[H\033[J")

    while True:
        try:
            background_mode = input(
                "Do you want to run the script in background mode ? (True/False): "
            )
            supported_backgroud_mode = ["False", "True", ""]
            if background_mode not in supported_backgroud_mode:
                raise Exception()
            if background_mode == "":
                background_mode = True
            else:
                background_mode = eval(background_mode)
            print("\033[H\033[J")
            break
        except:
            print("Please enter True or False")

    while True:
        try:
            sleep_time = input(
                "How many seconds do you want to wait between each login/logout ? (in seconds, default 3600, max 3600): "
            )
            supported_sleep_time = [str(i) for i in range(1, 3601)]
            supported_sleep_time.append("")
            if sleep_time not in supported_sleep_time:
                raise Exception()
            if sleep_time == "":
                sleep_time = 3600
            else:
                sleep_time = int(sleep_time)
            print("\033[H\033[J")
            break
        except:
            print("Please enter a number between 1 and 3600 seconds or leave empty")
    while True:
        try:
            print(
                "Configuration: \nEmail: {}\nPassword: {}\nBackground mode: {}\nSleep time: {} seconds".format(
                    email,
                    password.replace(password, "*" * len(password)),
                    background_mode,
                    sleep_time,
                )
            )
            confirm = input("Do you want to start the script ? (y/n): ")
            supported_confirm = ["y", "n"]
            if confirm not in supported_confirm:
                raise Exception()
            break
        except:
            print("Please enter y or n")
    if confirm == "n":
        print("\033[H\033[J")
        exit()
    while True:
        ka = KeepAlive(email, password, headless=background_mode)
        ka.login()
        sleep(sleep_time)
        ka.logout()
        del ka


if __name__ == "__main__":
    run()
