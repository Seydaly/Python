from address import Address
from mailing import Mailing


to_address = Address("инд. 777777", "Красноярск", "ул.Чкалова", "д.80", "кв.78")
from_address = Address("инд. 888888", "Москва", "ул.Тверская", "д.7", "кв.11")

mailing = Mailing(to_address, from_address, "5000", "посылка №070707")

print(f"Отправление {mailing.track} из: {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.flat} в: {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} -{mailing.to_address.flat}. Стоимость {mailing.cost} рублей.")
