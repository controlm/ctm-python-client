import abc
import getpass

__all__ = ['AbstractCredentials',
           'SimpleCredentials', 'InputPasswordCredentials']


class AbstractCredentials(abc.ABC):
    '''
    Abstract Class for Credentials

    Use to create your custom classes for more advanced use cases of authentication
    '''

    @abc.abstractclassmethod
    def get_username(self):
        pass

    @abc.abstractclassmethod
    def get_password(self):
        pass


class SimpleCredentials(AbstractCredentials):
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password


class InputPasswordCredentials(AbstractCredentials):
    def __init__(self, username: str):
        self.username = username

    def get_username(self):
        return self.username

    def get_password(self):
        return getpass.getpass(f'Enter the password for {self.username}')
