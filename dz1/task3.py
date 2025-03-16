class Stadium: 
    def __init__(self, title, data, country, city, capacity):
        self.title = title
        self.data = data
        self.country = country
        self.city = city
        self.capacity = capacity


    def input_data(self):
         self.title = input("введите название стадиона")
        self.data = int(input("введите дату выпуска"))
        self.country = input("введите страну")
        self.city = int(input("введите город"))
        self.capacity = input("введите вместительность")

    def otput_data(self):
        print(f"название: {self.title}")
        print(f"дата выпуска: {self.data}")
        print(f"страна: {self.country}")
        print(f"город: {self.city}")
        print(f"вместительность: {self.capacity} мест")

    def get_title(self)
        return self.title
    
    def get_data(self)
        return self.data

    def get_country(self)
        return self.country

    def get_city(self)
        return self.city

    def get_capacity(self)
        return self.capacity

    def set_title(self,title):
        self.title = title

    def set_data(self,data):
        self.data = data

    def set_country(self,country):
        self.country = country

    def set_city(self,city):
        self.city = city

    def set_capacity(self,capacity):
        self.capacity = capacity

stadium = Stadium("1989", 1999, "stars", "lolovo", 600 )
stadium.output_data()

stadium.set_capacity(600)
stadium.set_city("lolovo")
stadium.output_data()
