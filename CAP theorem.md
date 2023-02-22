**DragonFly**

DragonFly обеспечивает поддержку протоколов Redis, и ускоряет выполнение запросов с меньшим потреблением памяти.

Сама по себе система Redis является CP-системой (в случае сетевого раздела, Redis становится недоступным. В Redis Cluster(с помощью чего масштабируется) некоторая информация относится конкретному узлу и в конечном итоге согласуется во всем кластере. Вот почему с точки зрения CAP Redis — это CP)

- DragonFly подходит под условие *partition tolerance* аналогично Redis 
- Например, Redis SAVE останавливает обработку всех запросов по аналогии с FLUSHDB. В отличие от этого, DragonFly запускает его одновременно с остальным трафиком, при этом создавая согласованный моментальный снимок.
То есть он подходит под условие *consistency*

Значит, DragonFly является PC по теореме CAP

**ScyllaDB**

Эта система является PA по теореме CAP, ссылаясь на документацию (https://docs.scylladb.com/stable/architecture/architecture-fault-tolerance.html и https://www.scylladb.com/glossary/cap-theorem/).
Она удовлетворяет условиям *partition tolerance* и *availability*

**ArenadataDB**

* Одни из ее функциональных особенностей: транзакционность, возможность параллельной записи данных в сегменты кластера.
Требования к возможности транзакции является набор ACID. То есть, условие *consistency* должно быть выполнено. 
* Используется сервис YARN, который предоставляет большую доступность. Значит, условие *availability* тоже выполняется

Значит, система является CA по теореме CAP

Ссылки (https://arenadata.tech/products/arenadata-db/ и https://docs.arenadata.io/adh/administration/yarn/resourcemanager_ha_and_resizing.html)



