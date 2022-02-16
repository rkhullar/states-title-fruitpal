import httpx


async def async_httpx(method: str, *args, **kwargs):
    async with httpx.AsyncClient() as client:
        fn = getattr(client, method)
        return await fn(*args, **kwargs)
