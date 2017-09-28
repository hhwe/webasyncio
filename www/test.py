#-*- coding:utf-8 -*-

import orm, asyncio, sys
from models import User, Blog, Comment


@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop = loop, user = 'root', password = '12125772', db = 'awesome')
    # u = User(name='Administrator', email='admin@example.com', passwd='123', image='about:blank')
    u = User(id = '001494589233941fa76f44aa86f4343b17577411978ef8d000')
    # u = User(id = '')
    # yield from u.save()
    # yield from u.update()
    yield from u.remove()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete( asyncio.wait([test( loop )]) )  
    loop.close()
    if loop.is_closed():
        sys.exit(0)