from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._queue: list[tuple[int, str]] = []
        self._processed_count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        raise NotImplementedError

    @abstractmethod
    def ingest(self, data: Any) -> None:
        raise NotImplementedError

    def _store(self, value: str) -> None:
        rank = self._processed_count
        self._queue.append((rank, value))
        self._processed_count += 1

    def output(self) -> tuple[int, str]:
        if not self._queue:
            raise ValueError("No data available")
        return self._queue.pop(0)

    def remaining(self) -> int:
        return len(self._queue)

    def total_processed(self) -> int:
        return self._processed_count

    def processor_name(self) -> str:
        return self.__class__.__name__.replace("Processor", " Processor")


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for value in data:
                self._store(str(value))
            return
        self._store(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for value in data:
                self._store(value)
            return
        self._store(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self._is_log_dict(data)
        if isinstance(data, list):
            return all(
                isinstance(x, dict) and self._is_log_dict(x) for x in data
                )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for entry in data:
                self._store(self._format_log(entry))
            return
        self._store(self._format_log(data))

    def _is_log_dict(self, data: dict[Any, Any]) -> bool:
        return all(
            isinstance(k, str) and isinstance(v, str) for k, v in data.items()
            )

    def _format_log(self, entry: dict[str, str]) -> str:
        level = entry.get("log_level", "INFO")
        message = entry.get("log_message", "")
        return f"{level}: {message}"


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(
                    "DataStream error- Can't process "
                    f"element in stream: {element}"
                    )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(
                f"{proc.processor_name()}: total {proc.total_processed()}"
                "items processed, "
                f"remaining {proc.remaining()} on processor"
            )


def main() -> None:
    print("=== Code Nexus- Data Stream ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    numeric = NumericProcessor()
    print("Registering Numeric Processor")
    stream.register_processor(numeric)

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
                },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("Registering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(text)
    stream.register_processor(log)

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
        )
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    for _ in range(1):
        log.output()
    stream.print_processors_stats()

    print(
        "How does polymorphism allow DataStream to process mixed data cleanly?"
        )
    print(
        "It calls the same validate/ingest"
        " interface on each registered processor."
        )


if __name__ == "__main__":
    main()
