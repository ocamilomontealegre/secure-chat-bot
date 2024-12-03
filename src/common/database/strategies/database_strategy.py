from abc import ABC, abstractmethod

class DatabaseStrategy(ABC):
    @abstractmethod
    def create_engine(self):
        """Method to create a database engine"""
        pass

    @abstractmethod
    def create_session(self):
        """Method to create a session"""
        pass

    @abstractmethod
    def get_connection_url(self):
        """Method to get the connection url"""
        pass
