from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from gateway import GatewayContainer
from services import ServiceContainer
from settings import settings


class MainContainer(DeclarativeContainer):
    config = providers.Object(settings)
    gateway_container = providers.Container(
        GatewayContainer,
        config=config,
    )
    service_container = providers.Container(
        ServiceContainer,
        config=config,
    )
