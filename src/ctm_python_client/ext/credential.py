from ctm_python_client.core.credential import AbstractCredentials

import keyring

__all__ = ['KeyringCredentials']

class KeyringCredentials(AbstractCredentials):
    def __init__(self, service: str, username: str) -> None:
        super().__init__()

        self.service = service
        self.username = username

    def get_username(self):
        return self.username

    def get_password(self):
        return keyring.get_password(self.service, self.username)
