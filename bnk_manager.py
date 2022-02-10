from datetime import datetime
import month


class BNKManager():
    def __init__(self, members):
        self.members = members

    def get_name(self, member, lang):
        return (f"{member['first_name'][lang]} {member['last_name'][lang]}")

    def get_data(self, props):
        data = []
        for member in self.members:
            member_details = {}
            for prop in props:
                member_details[prop] = member[prop]
            data.append(member_details)
        return data

    def display_name(self, reverse=True, lang='en'):
        members_name = self.get_data({'first_name', 'last_name'})
        members_name = map(lambda name: self.get_name(
            name, lang), members_name)
        members_name = sorted(members_name, reverse=reverse, key=len)

        for name in members_name:
            print(name)

    def display_month(self):
        members = self.get_data({'birth_date', 'first_name', 'last_name'})

        members = list(map(
            (lambda a: {'month': datetime.utcfromtimestamp(int(a['birth_date'])/1000).strftime('%m'), 'name': self.get_name(a, 'en')}), members))
        most = self.get_most_month(members)

        print('most:', month.MONTH[int(most)])

        for member in members:
            if member['month'] == most:
                print(member['name'])

    def get_most_month(self, members):
        count_month = {}

        for member in members:
            month = member['month']
            if count_month.get(month) is None:
                count_month[month] = 0
            count_month[month] += 1

        return max(count_month, key=count_month.get)
