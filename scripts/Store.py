class Store:
      def __init__(self, store):
            self.addr = store['addr']
            self.title = store['title']
            self.price = store['price']
            self.area = store['area']
            self.srv_rate = store['srv_rate']
            self.env_rate = store['env_rate']
            self.flavor_rate = store['flavor_rate']
            self.num_comment = store['num_comment']
            self.dish_type = store['dish_type']

      def __cmp__(self, other):
            self_rate = (float(self.flavor_rate) + float(self.env_rate) +float(self.srv_rate))/3. 
            other_rate = (float(other.flavor_rate) + float(other.env_rate) +float(other.srv_rate))/3.
            return self_rate < other_rate  
