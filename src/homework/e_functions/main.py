#
from value_return import get_hour, get_minutes, get_seconds

def main():
    epoch_seconds = 3800

    hours = get_hour(epoch_seconds)
    minutes = get_minutes(epoch_seconds)
    seconds = get_seconds(epoch_seconds)

    print(f"The time is:  {hours:02d}:{minutes:02d}:{seconds:02d}" )

main()

