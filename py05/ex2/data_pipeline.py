from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CsvExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        line = ",".join(value for _, value in data)
        print("CSV Output:")
        print(line)


class JsonExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        parts: list[str] = []
        for rank, value in data:
            escaped = value.replace("\\", "\\\\").replace('"', '\\"')
            parts.append(f"\"item_{rank}\": \"{escaped}\"")
        print("JSON Output:")
        print("{" + ", ".join(parts) + "}")


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
                    "DataStream error-"
                    f" Can't process element in stream: {element}"
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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            pulled: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc.remaining() == 0:
                    break
                pulled.append(proc.output())
            if pulled:
                plugin.process_output(pulled)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    print("Registering Processors")
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    batch_1: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message":
             "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch_1}")
    stream.process_stream(batch_1)
    stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CsvExportPlugin())
    stream.print_processors_stats()

    batch_2: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE", "log_message":
                "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"Send another batch of data: {batch_2}")
    stream.process_stream(batch_2)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JsonExportPlugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
