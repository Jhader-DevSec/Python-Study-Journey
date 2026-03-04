import asyncio

async def worker(task_name, delay):
    print(f"[*] Initiating {task_name} (Delay: {delay}s)...")
    await asyncio.sleep(delay)
    print(f"[+] {task_name} has been completed!")
    return f"{task_name} SUCCESS"

async def main():
    print("--- Starting Async Tasks ---")
    result = await asyncio.gather(
        worker("Task-A", 1),
        worker("Task-B", 5),
        worker("Task-C", 10)
    )
    
    print("\n--- All tasks finished ---")
    print(f"Gather Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())