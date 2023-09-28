class Room:
    def __init__(self, room_type, price):
        self.room_type = room_type
        self.price = price
        self.is_occupied = False

class Guest:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Service:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Review:
    def __init__(self, guest_name, text):
        self.guest_name = guest_name
        self.text = text

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.services = []
        self.child_services = []
        self.reviews = []

    def add_room(self, room_type, price):
        new_room = Room(room_type, price)
        self.rooms.append(new_room)

    def add_service(self, name, price):
        new_service = Service(name, price)
        self.services.append(new_service)

    def add_child_service(self, name, price):
        new_service = Service(name, price)
        self.child_services.append(new_service)

    def add_review(self, guest_name, text):
        new_review = Review(guest_name, text)
        self.reviews.append(new_review)

    def get_vacant_rooms(self):
        return [room for room in self.rooms if not room.is_occupied]

    def book_room(self, guest_name, age, room_type):
        vacant_rooms = self.get_vacant_rooms()
        for room in vacant_rooms:
            if room.room_type == room_type:
                room.is_occupied = True
                return f"Кімната {room_type} заброньована на ім'я {guest_name}"
        return f"Вільних кімнат типу {room_type} немає"

    def show_rooms(self):
        for room in self.rooms:
            status = "Вільна" if not room.is_occupied else "Зайнята"
            print(f"Тип кімнати: {room.room_type} - Ціна: {room.price} - Статус: {status}")

    def show_services(self):
        print("Основні послуги:")
        for service in self.services:
            print(f"Послуга: {service.name} - Ціна: {service.price}")

        print("\nДитячі послуги:")
        for service in self.child_services:
            print(f"Послуга: {service.name} - Ціна: {service.price}")

    def show_reviews(self):
        for review in self.reviews:
            print(f"Гість: {review.guest_name} - Відгук: {review.text}")

if __name__ == "__main__":
    my_hotel = Hotel("IT STEP")
    my_hotel.add_room("Стандарт", 100)
    my_hotel.add_room("Люкс", 200)
    my_hotel.add_room("Бізнес", 150)
    my_hotel.add_service("Спа", 50)
    my_hotel.add_service("Тренажерний зал", 20)
    my_hotel.add_service("Ресторан", 30)
    my_hotel.add_child_service("Дитячий клуб", 25)
    my_hotel.add_child_service("Дитячий басейн", 10)
    my_hotel.add_child_service("Послуги няні", 20)
    my_hotel.add_review("Іван", "Чудовий готель!")
    my_hotel.add_review("Олена", "Жахливие обслуговування!")
    my_hotel.show_rooms()
    my_hotel.show_services()
    my_hotel.show_reviews()
