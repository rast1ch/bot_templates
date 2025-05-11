from collections.abc import AsyncGenerator
from contextlib import (
    AbstractContextManager,
    asynccontextmanager,
    contextmanager,
)

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import NullPool


class SyncDatabase:
    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url, pool_pre_ping=True, echo=False)
        self._session_factory = sessionmaker(
            bind=self._engine,
            autocommit=False,
            autoflush=False,
        )

    @contextmanager  # type: ignore
    def session(self) -> AbstractContextManager[Session]:  # type: ignore
        session: Session = self._session_factory()
        try:
            yield session  # type: ignore
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


class AsyncDatabase:
    def __init__(self, db_url: str) -> None:
        self._engine = create_async_engine(
            db_url,
            poolclass=NullPool,
            echo=False,
        )
        self._session_factory = async_sessionmaker(
            self._engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
        )

    @asynccontextmanager
    async def session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self._session_factory() as session:
            try:
                yield session
            except Exception:
                await session.rollback()
                raise
            finally:
                await session.close()
