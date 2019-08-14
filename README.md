# Redis proxy service

## Architecture

Used Flask to create a GET, PUT, and DELETE that interfaced with redis.

Configuration per environment can be done in the `config` file

##

## Algorithmic complexity

I went for the simplest solution I could find based on what seemed like common libraries for this use case.
Flask being the common REST API library for python, I relied on that.

Flask has built in functionality to handle parallelism.

## Running Tests

```
Make Tests
```

## Time Allocation

Reading Comprehension
* The bulk of my time was spent reading and understanding the assignment more than anything.
Writing a proxy service is unfamiliar to me, so I wanted to make sure I understood the assignment
to the best of my abilities before beginning.

* Spinning up the local Redis was trivial

* Finding the right LRU Cache library and then implementing it was a pain

* Spent a lot of time trying to figure out how to implement Concurrency before realizing
Flask had built-in functionality to handle that

* Unit tests
I honestly had no idea how to test concurrency or ensuring something was indeed being pulled from cache or ttl

Total time spent was ~8 hours

## Omitted Requirements

* Could not figure out how to test threading. Spawned a bunch of calls that appear to succeed but the total threadcount kept returning as 1.

