**DragonFly**

DragonFly обеспечивающей поддержку протоколов Memcached и Redis, но позволяющей выполнять запросы с гораздо более высокой производительностью и с меньшим потреблением памяти
Например, Redis SAVE останавливает обработку всех запросов по аналогии с FLUSHDB. В отличие от этого, DragonFly запускает его одновременно с остальным трафиком, при этом создавая согласованный моментальный снимок.
То есть он подходит под условие 'consistency'

Redis имеет архитектуру Master-Slave, и если Master выходит из строя, то Redis Sentinels продвигает Slave в качестве нового Master, делая все решение высокодоступным. И мастер может выйти из строя (или стать недоступным) по ряду причин (например, из-за нехватки памяти), это не обязательно связано с сетевым разделом.

Затем наступает случай сетевого раздела (P), и если (P) происходит, Redis становится недоступным в миноритарном разделе. Вот почему с точки зрения CAP Redis — это CP, потому что он становится недоступным в разделах меньшинства. Обратите внимание, что он по-прежнему будет доступен в большинстве разделов.



