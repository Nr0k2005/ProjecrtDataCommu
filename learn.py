from contextlib import contextmanager
import time

@contextmanager
def timer():
    import time
    start = time.time()
    yield                          # ← ตรงนี้คือ block ของ with
    print(f"ใช้เวลา {time.time() - start:.2f}s")

with timer():
    # โค้ดที่ต้องจับเวลา
    time.sleep(1)  # ตัวอย่าง: นอนหลับ 1 วินาที
    print("ทำงานเสร็จแล้ว!")
    time.sleep(2)  # ตัวอย่าง: นอนหลับอีก 2 วินาที
    print("ทำงานเสร็จแล้วอีกครั้ง!")