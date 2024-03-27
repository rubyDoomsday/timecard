from .utils import client

def run(config, args):
    Timecard(config, args).run()

class Timecard:
    def __init__(self, config, args):
        self.config = config
        self.args = args

    def run(self):
        if self.args.copy == None:
            self.submit_week(self.args.date, self.args.hours)
        else:
            self.__copy_last_week(self.args.date)
        print("done")

    def submit_week(self, date, hours):
        _hours = self.__parse_hours(hours)
        print(f'create new hours for -> {date}: {_hours}')
        self.__client().submit_week(date, _hours)

    def __copy_last_week(self, date):
        print(f'copy last week to this week -> {date}')
        self.__client().copy_last_week(date)

    def __parse_hours(self, hours):
        result_dict = {}
        for i in range(0, len(hours), 2):
            key = hours[i]
            value = int(hours[i+1])
            result_dict[key] = value

        return result_dict

    def __client(self):
        return client.Client(self.config)
