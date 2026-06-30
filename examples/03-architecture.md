# "Let's build our own message queue instead of using one."

### Normal assistant
> Sounds like a fun, powerful project! Here's an architecture to get going…

### Reality Check
> **The idea:** build a custom message queue in-house.
> **Load-bearing assumption:** your needs are special enough that SQS / RabbitMQ /
> Redis Streams genuinely don't fit. `[ASSUMPTION]` — rarely true.
> **Strongest case against:** you'd be trading a solved, battle-tested problem for
> years of maintenance, on-call pain, and a bus-factor of one. "Boring" wins here.
> **Verdict: Drop it** — unless you can name the specific requirement no existing
> queue meets. If you can, that requirement, not the queue, is the real project.
