import pytest # type: ignore[import-not-found]
from src.calculator import Calculator, DataProcessor

# 基本的なテスト
def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

# パラメータ化テスト
@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (0, 5, 0),
    (-2, -3, 6),
])
def test_multiply(a, b, expected):
    calc = Calculator()
    assert calc.multiply(a, b) == expected

# 例外テスト
def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(1, 0)

# フィクスチャの使用例
@pytest.fixture
def calculator():
    return Calculator()

def test_with_fixture(calculator):
    assert calculator.add(3, 4) == 7

# 非同期テストの例
@pytest.mark.asyncio
async def test_process_numbers():
    processor = DataProcessor()
    result = await processor.process_numbers([1, 2, 3])
    assert result == [2, 4, 6]
