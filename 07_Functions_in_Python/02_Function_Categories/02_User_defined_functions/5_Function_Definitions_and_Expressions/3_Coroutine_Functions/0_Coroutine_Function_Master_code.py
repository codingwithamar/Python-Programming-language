# =============================================================================
# Author      : codingwithamar@gmail.com
# File        : 1_Coroutine_Function_Complete_Guide.py
# Path        : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/3_Coroutine_Function/
# Subject     : User Defined Functions
# Description : Coroutine Functions / Complete Concepts and Practical Examples
# Python      : 3.11+
# =============================================================================
#
# TOPICS COVERED
#   1. async and await keywords
#   2. Coroutine function definition and coroutine object creation
#   3. Coroutine execution with asyncio.run()
#   4. Awaiting a coroutine and returning values
#   5. Forgetting await
#   6. Sequential execution
#   7. Concurrent execution with asyncio.gather()
#   8. Creating and managing Tasks
#   9. Task inspection and result methods
#  10. Task cancellation and CancelledError
#  11. asyncio.wait(), FIRST_COMPLETED, ALL_COMPLETED
#  12. asyncio.as_completed()
#  13. Timeouts with asyncio.wait_for() and asyncio.timeout()
#  14. asyncio.shield()
#  15. Coroutine and awaitable inspection
#  16. Coroutine states and close()
#  17. Driving a coroutine with send() (low-level demonstration)
#  18. Exception handling in coroutines
#  19. TaskGroup and structured concurrency
#  20. ExceptionGroup and except*
#  21. Synchronization: Lock, Event, Semaphore, Condition
#  22. Async context managers (async with)
#  23. Async iterators (__aiter__, __anext__)
#  24. Async generators (async def + yield)
#  25. Async comprehensions
#  26. Async queues: Queue, task_done(), join()
#  27. Running blocking work with asyncio.to_thread()
#  28. Event loop basics and asyncio debug mode
#
# NOTE:
#   - This is a learning/demo file. Run it as a normal Python script.
#   - Output order can vary for concurrent examples.
#   - asyncio.run() should normally be called once at the program entry point.
# =============================================================================

import asyncio
import inspect
import keyword
import time


# =============================================================================
# 1. COROUTINE FUNCTION AND COROUTINE OBJECT
# =============================================================================

async def get_value():
    # async def defines a coroutine function.
    return 42


async def example_coroutine_basics():
    coro = get_value()

    print("Is coroutine function:",
          inspect.iscoroutinefunction(get_value))  # True
    print("Is coroutine object:",
          inspect.iscoroutine(coro))               # True
    print("Coroutine type:", type(coro))

    result = await coro
    print("Coroutine return value:", result)       # 42


# =============================================================================
# 2. await AND ASYNCHRONOUS SUSPENSION
# =============================================================================

async def say_after(delay, message):
    await asyncio.sleep(delay)
    print(message)
    return message


async def example_await():
    result = await say_after(0.1, "Finished after await")
    print("Returned:", result)


# =============================================================================
# 3. FORGETTING await - COMMON MISTAKE
# =============================================================================

async def example_forgetting_await():
    coro = get_value()  # Creates a coroutine object; does not run its body.
    print("Created but not awaited:", inspect.iscoroutine(coro))

    result = await coro
    print("After awaiting:", result)

    # Avoid leaving a coroutine unawaited: this example awaits it correctly.


# =============================================================================
# 4. SEQUENTIAL EXECUTION
# =============================================================================

async def example_sequential():
    start = time.perf_counter()

    a = await say_after(0.15, "Sequential A")
    b = await say_after(0.15, "Sequential B")
    c = await say_after(0.15, "Sequential C")

    print("Sequential results:", a, b, c)
    print(f"Sequential elapsed: {time.perf_counter() - start:.2f}s")


# =============================================================================
# 5. CONCURRENT EXECUTION - asyncio.gather()
# =============================================================================

async def example_gather():
    start = time.perf_counter()

    results = await asyncio.gather(
        say_after(0.3, "Concurrent A"),
        say_after(0.1, "Concurrent B"),
        say_after(0.2, "Concurrent C"),
    )

    print("gather results:", results)
    print(f"Concurrent elapsed: {time.perf_counter() - start:.2f}s")


# =============================================================================
# 6. TASK CREATION - asyncio.create_task()
# =============================================================================

async def example_create_task():
    task = asyncio.create_task(say_after(0.1, "Task finished"))

    print("Is Task:", isinstance(task, asyncio.Task))
    print("Task name:", task.get_name())

    print("Main coroutine continues while task is scheduled")
    result = await task
    print("Task result:", result)


# =============================================================================
# 7. TASK STATUS AND RESULT METHODS
# =============================================================================

async def example_task_inspection():
    task = asyncio.create_task(get_value())

    print("Initially done:", task.done())

    result = await task

    print("Done:", task.done())
    print("Cancelled:", task.cancelled())
    print("Task result():", task.result())
    print("Await result:", result)


# =============================================================================
# 8. TASK CANCELLATION - cancel() AND CancelledError
# =============================================================================

async def cancellation_worker():
    try:
        print("Worker started")
        await asyncio.sleep(5)
        print("Worker completed normally")
    except asyncio.CancelledError:
        print("Worker received cancellation")
        raise  # Propagate cancellation after cleanup.


async def example_task_cancellation():
    task = asyncio.create_task(cancellation_worker())

    await asyncio.sleep(0.05)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Main: cancellation handled")

    print("Task cancelled:", task.cancelled())


# =============================================================================
# 9. asyncio.wait()
# =============================================================================

async def example_wait():
    task_a = asyncio.create_task(say_after(0.1, "wait A"))
    task_b = asyncio.create_task(say_after(0.25, "wait B"))

    done, pending = await asyncio.wait(
        {task_a, task_b},
        return_when=asyncio.FIRST_COMPLETED,
    )

    print("FIRST_COMPLETED - done:", len(done))
    print("FIRST_COMPLETED - pending:", len(pending))

    # Wait for remaining tasks to finish.
    if pending:
        await asyncio.wait(pending, return_when=asyncio.ALL_COMPLETED)


# =============================================================================
# 10. asyncio.as_completed()
# =============================================================================

async def example_as_completed():
    coroutines = [
        say_after(0.25, "as_completed A"),
        say_after(0.05, "as_completed B"),
        say_after(0.15, "as_completed C"),
    ]

    for completed in asyncio.as_completed(coroutines):
        result = await completed
        print("Received as completed:", result)


# =============================================================================
# 11. TIMEOUTS - wait_for() AND asyncio.timeout()
# =============================================================================

async def slow_operation():
    await asyncio.sleep(1)
    return "Slow operation result"


async def example_timeouts():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=0.05)
        print(result)
    except asyncio.TimeoutError:
        print("wait_for: operation timed out")

    try:
        async with asyncio.timeout(0.05):
            await asyncio.sleep(1)
    except TimeoutError:
        print("asyncio.timeout: operation timed out")


# =============================================================================
# 12. asyncio.shield()
# =============================================================================

async def example_shield():
    protected_task = asyncio.create_task(say_after(0.15, "Shielded task finished"))

    try:
        # wait_for times out, but shield prevents it from cancelling the task.
        await asyncio.wait_for(asyncio.shield(protected_task), timeout=0.02)
    except asyncio.TimeoutError:
        print("Caller timed out; protected task continues")

    result = await protected_task
    print("Shielded task result:", result)


# =============================================================================
# 13. COROUTINE INSPECTION AND STATES
# =============================================================================

async def example_coroutine_inspection():
    coro = get_value()

    print("is coroutine function:",
          inspect.iscoroutinefunction(get_value))
    print("is coroutine:",
          inspect.iscoroutine(coro))
    print("is awaitable:",
          inspect.isawaitable(coro))
    print("Initial state:",
          inspect.getcoroutinestate(coro))  # CORO_CREATED

    coro.close()
    print("After close:",
          inspect.getcoroutinestate(coro))  # CORO_CLOSED


# =============================================================================
# 14. LOW-LEVEL COROUTINE send(None) DEMONSTRATION
# =============================================================================

async def immediate_result():
    return "completed by send(None)"


async def example_coroutine_send():
    coro = immediate_result()

    try:
        coro.send(None)
    except StopIteration as stop:
        print("send(None) return value:", stop.value)


# =============================================================================
# 15. EXCEPTION HANDLING IN COROUTINES
# =============================================================================

async def risky_operation(number):
    if number < 0:
        raise ValueError("number must not be negative")
    return number * 2


async def example_exception_handling():
    print("Valid result:", await risky_operation(5))

    try:
        await risky_operation(-1)
    except ValueError as error:
        print("Caught exception:", error)


# =============================================================================
# 16. STRUCTURED CONCURRENCY - asyncio.TaskGroup
# =============================================================================

async def example_task_group():
    async with asyncio.TaskGroup() as group:
        task_a = group.create_task(say_after(0.1, "TaskGroup A"))
        task_b = group.create_task(say_after(0.15, "TaskGroup B"))

    # Exiting TaskGroup waits for its child tasks.
    print("TaskGroup results:", task_a.result(), task_b.result())


# =============================================================================
# 17. ExceptionGroup AND except*
# =============================================================================

async def raise_value_error():
    raise ValueError("ValueError from child task")


async def raise_type_error():
    raise TypeError("TypeError from child task")


async def example_exception_group():
    try:
        async with asyncio.TaskGroup() as group:
            group.create_task(raise_value_error())
            group.create_task(raise_type_error())
    except* ValueError as errors:
        print("Handled ValueError group:", len(errors.exceptions))
    except* TypeError as errors:
        print("Handled TypeError group:", len(errors.exceptions))


# =============================================================================
# 18. SYNCHRONIZATION - asyncio.Lock
# =============================================================================

async def example_lock():
    lock = asyncio.Lock()
    counter = 0

    async def increment():
        nonlocal counter
        async with lock:
            current = counter
            await asyncio.sleep(0.01)
            counter = current + 1

    await asyncio.gather(*(increment() for _ in range(5)))
    print("Counter protected by Lock:", counter)


# =============================================================================
# 19. SYNCHRONIZATION - asyncio.Event
# =============================================================================

async def example_event():
    event = asyncio.Event()

    async def waiter():
        print("Waiter: waiting for event")
        await event.wait()
        print("Waiter: event received")

    task = asyncio.create_task(waiter())
    await asyncio.sleep(0.05)
    event.set()
    await task


# =============================================================================
# 20. SYNCHRONIZATION - asyncio.Semaphore
# =============================================================================

async def example_semaphore():
    semaphore = asyncio.Semaphore(2)

    async def worker(number):
        async with semaphore:
            print(f"Semaphore worker {number}: entered")
            await asyncio.sleep(0.05)
            print(f"Semaphore worker {number}: leaving")

    await asyncio.gather(*(worker(i) for i in range(1, 5)))


# =============================================================================
# 21. SYNCHRONIZATION - asyncio.Condition
# =============================================================================

async def example_condition():
    condition = asyncio.Condition()
    state = {"ready": False}

    async def waiter():
        async with condition:
            await condition.wait_for(lambda: state["ready"])
            print("Condition: ready signal received")

    async def notifier():
        await asyncio.sleep(0.05)
        async with condition:
            state["ready"] = True
            condition.notify_all()

    await asyncio.gather(waiter(), notifier())


# =============================================================================
# 22. ASYNC CONTEXT MANAGER - async with
# =============================================================================

class AsyncResource:
    async def __aenter__(self):
        print("Async resource opened")
        await asyncio.sleep(0.02)
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        print("Async resource closed")
        await asyncio.sleep(0.02)
        return False  # Do not suppress exceptions.


async def example_async_context_manager():
    async with AsyncResource() as resource:
        print("Using:", type(resource).__name__)


# =============================================================================
# 23. ASYNC ITERATOR - __aiter__() AND __anext__()
# =============================================================================

class AsyncCounter:
    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.limit:
            raise StopAsyncIteration

        await asyncio.sleep(0.02)
        self.current += 1
        return self.current


async def example_async_iterator():
    async for number in AsyncCounter(3):
        print("Async iterator value:", number)


# =============================================================================
# 24. ASYNC GENERATOR - async def + yield
# =============================================================================

async def async_countdown(start):
    while start > 0:
        await asyncio.sleep(0.02)
        yield start
        start -= 1


async def example_async_generator():
    agen = async_countdown(3)

    print("Is async generator function:",
          inspect.isasyncgenfunction(async_countdown))
    print("Is async generator:",
          inspect.isasyncgen(agen))

    async for value in agen:
        print("Async generator value:", value)


# =============================================================================
# 25. ASYNC COMPREHENSION
# =============================================================================

async def async_values():
    for value in range(1, 4):
        await asyncio.sleep(0.01)
        yield value


async def example_async_comprehension():
    values = [value async for value in async_values()]
    print("Async list comprehension:", values)


# =============================================================================
# 26. ASYNC QUEUE - Producer / Consumer
# =============================================================================

async def example_queue():
    queue = asyncio.Queue()

    async def producer():
        for item in range(1, 4):
            await queue.put(item)
            print("Produced:", item)
        await queue.put(None)  # Sentinel: tells consumer to stop.

    async def consumer():
        while True:
            item = await queue.get()
            try:
                if item is None:
                    return
                print("Consumed:", item)
            finally:
                queue.task_done()

    producer_task = asyncio.create_task(producer())
    consumer_task = asyncio.create_task(consumer())

    await producer_task
    await queue.join()
    await consumer_task


# =============================================================================
# 27. RUN BLOCKING FUNCTION WITHOUT BLOCKING EVENT LOOP - to_thread()
# =============================================================================

def blocking_function():
    time.sleep(0.1)
    return "Blocking function completed in a worker thread"


async def example_to_thread():
    result = await asyncio.to_thread(blocking_function)
    print(result)


# =============================================================================
# 28. EVENT LOOP AND DEBUG MODE
# =============================================================================

async def example_event_loop():
    loop = asyncio.get_running_loop()
    print("Running loop:", type(loop).__name__)
    print("Debug mode:", loop.get_debug())


# =============================================================================
# KEYWORD CHECK
# =============================================================================

def example_keywords():
    print("async is keyword:", keyword.iskeyword("async"))
    print("await is keyword:", keyword.iskeyword("await"))


# =============================================================================
# MAIN COROUTINE
# =============================================================================

async def main():
    examples = [
        ("1. Coroutine basics", example_coroutine_basics),
        ("2. await expression", example_await),
        ("3. Forgetting await", example_forgetting_await),
        ("4. Sequential execution", example_sequential),
        ("5. Concurrent execution - gather", example_gather),
        ("6. Task creation", example_create_task),
        ("7. Task inspection", example_task_inspection),
        ("8. Task cancellation", example_task_cancellation),
        ("9. asyncio.wait", example_wait),
        ("10. asyncio.as_completed", example_as_completed),
        ("11. Timeouts", example_timeouts),
        ("12. asyncio.shield", example_shield),
        ("13. Coroutine inspection and states", example_coroutine_inspection),
        ("14. Coroutine send(None)", example_coroutine_send),
        ("15. Exception handling", example_exception_handling),
        ("16. TaskGroup", example_task_group),
        ("17. ExceptionGroup and except*", example_exception_group),
        ("18. asyncio.Lock", example_lock),
        ("19. asyncio.Event", example_event),
        ("20. asyncio.Semaphore", example_semaphore),
        ("21. asyncio.Condition", example_condition),
        ("22. Async context manager", example_async_context_manager),
        ("23. Async iterator", example_async_iterator),
        ("24. Async generator", example_async_generator),
        ("25. Async comprehension", example_async_comprehension),
        ("26. Async Queue", example_queue),
        ("27. asyncio.to_thread", example_to_thread),
        ("28. Event loop basics", example_event_loop),
    ]

    for title, example in examples:
        print(f"\\n{'=' * 18} {title} {'=' * 18}")
        await example()

    print("\\n==================== Keyword checks ====================")
    example_keywords()


if __name__ == "__main__":
    # asyncio.run() creates the event loop, runs main(), then closes the loop.
    # Do not call asyncio.run() from inside an already-running event loop.
    asyncio.run(main())
