from dataclasses import dataclass
import json


@dataclass()
class Configuration:
    postgres_secrets: str
    postgres_host: str

    @classmethod
    def read_from(cls, configuration_file_path):
        with open(configuration_file_path) as config:
            data = json.loads(config.read())
            return Configuration(
                postgres_host=data['postgres'],
                postgres_secrets=data['postgres_secrets']
            )
