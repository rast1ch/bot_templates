from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from .db import AsyncDatabase, SyncDatabase


class GatewayContainer(DeclarativeContainer):
    """Gateway container for dependency injection."""

    config = providers.Configuration()

    sync_session = providers.Singleton(
        SyncDatabase,
        db_url=config.DATABASE_URL,
    )

    async_session = providers.Singleton(
        AsyncDatabase,
        db_url=config.DATABASE_URL,
    )
