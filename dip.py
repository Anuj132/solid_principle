'''
 The Dependency Inversion Principle (DIP)

“Abstractions should not depend on details.
Details should depend on abstraction. High-level modules should not depend on low-level
 modules. Both should depend on abstractions”
'''

class DeliveryDriver(object):

    def deliver_product(self, product):
        # Deliver product...
        pass


class DeliveryCompany(object):

    def send_product(self, product):
        delivery_driver = DeliveryDriver()
        delivery_driver.deliver_product(product)

'''
Above code is not satisfied DIP property.

Below code is satisfied the DIP property.
'''

from abc import ABC, abstractmethod


class DeliveryService(ABC):


    @abstractmethod
    def deliver_product(self, product):
        pass


class DeliveryDriver(DeliveryService):

    def deliver_product(self, product):
        # Implement deliver
        pass


class DeliveryCompany(object):

    def __init__(self, delivery_service):
        self.delivery_service = delivery_service

    def send_product(self, product):
        self.delivery_service.deliver_product(product)