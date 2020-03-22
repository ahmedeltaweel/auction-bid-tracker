'''
Dummy model representing DB
'''


class User:
    """
    In memory database table representing users.
    """

    def __init__(self):
        self._id = 1
        self.table = dict()

    def __str__(self):
        """
        String representation of the Database table
        """
        return str(self.__dict__)

    def get(self, id):
        return self.table.get(id, None)

    def add(self, user=dict()):
        """
        Adds a user to the table.
        """
        self.table.update({self._id: user})
        self._id += 1

    def remove(self, user):
        """
        Removes user from table.
        """
        return self.table.pop(user['id'], None)


class Item:
    """
    In memory database table representing Item.
    """

    def __init__(self):
        self._id = 1
        self.table = dict()

    def __str__(self):
        """
        String representation of the Database table
        """
        return str(self.__dict__)

    def get(self, id):
        return self.table.get(id, None)

    def add(self, item=dict()):
        """
        Adds a user to the table.
        """
        self.table.update({self._id: item})
        self._id += 1

    def remove(self, item):
        """
        Removes item from table.
        """
        return self.table.pop(item['id'], None)


class Bid:
    """
    In memory database table representing Bid.
    """

    def __init__(self):
        self._id = 1
        self.table = dict()

    def __str__(self):
        """
        String representation of the Database table
        """
        return str(self.__dict__)

    def get(self, id):
        return self.table.get(id, None)

    def add(self, bid=dict()):
        """
        Adds a user to the table.
        """
        self.table.update({self._id: bid})
        self._id += 1

    def remove(self, bid):
        """
        Removes bid from table.
        """
        return self.table.pop(bid['id'], None)

    def get_all_for_item(self, item_id):
        """
        Return all bids for item
        """
        return [self.table[bid] for bid in self.table if self.table[bid]['item_id'] == item_id]

    def get_all_for_user(self, user_id):
        """
        Return all bids for user
        """
        return [self.table[bid] for bid in self.table if self.table[bid]['user_id'] == user_id]

    def get_winning_bid(self, item_id):
        """
        Return current winning bids for item
        """
        all_bids = [self.table[bid] for bid in self.table if self.table[bid]['item_id'] == item_id]
        return max(all_bids, key=lambda x: x['amount'])
