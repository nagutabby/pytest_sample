class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b

    def divide(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def multiply(self, a: int, b: int) -> int:
        return a * b

# 応用例として非同期関数も追加
import asyncio

class DataProcessor:
    async def process_numbers(self, numbers: list[int]) -> list[int]:
        # 数値のリストを受け取って2倍にする非同期処理の例
        await asyncio.sleep(0.1)  # 非同期処理のシミュレーション
        return [num * 2 for num in numbers]
