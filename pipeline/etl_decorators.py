import time
import random
# RETRY DECORATOR WITH PARAMETERS
def retry(max_attempts=3, delay=1):
    def actual_decorator(some_function):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    result = some_function(*args, **kwargs)
                    # If we get here, it succeeded
                    print(f"✅ Attempt {attempt} succeeded")
                    return result
                except Exception as error:
                    print(f"❌ Attempt {attempt} failed: {error}")
                    if attempt == max_attempts:
                        # WHAT GOES HERE? (This is the last attempt, all failed)
                        print(f"💥 All {max_attempts} attempts failed!")
                        raise error
                    else:
                        # Not the last attempt, wait and try again
                        # YOUR CODE HERE (Hint: use time.sleep)
                        time.sleep(delay)
        return wrapper
    return actual_decorator
# TEST: Function that fails randomly
@retry(max_attempts=4, delay=0.3)
def fetch_data_from_api():
    if random.random() < 0.6:  # 60% chance of failure
        raise ConnectionError("API timeout!")
    return {"status": "success", "data": [1, 2, 3]}


# RUN IT
print("=" * 40)
try:
    result = fetch_data_from_api()
    print(f"🎉 Final result: {result}")
except ConnectionError as e:
    print(f"🚫 Could not fetch data: {e}")