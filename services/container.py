from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer


class ServiceContainer(DeclarativeContainer):
    config = providers.Dependency()
