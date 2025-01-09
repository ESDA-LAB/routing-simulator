from abc import ABC, abstractmethod
from typing import List, Tuple

class ShortestPathInterface(ABC):
    @abstractmethod
    def FindRoute(self, start: Tuple[int, int], end: Tuple[int, int], obstacles: List[Tuple[int, int]], 
                  map_size: Tuple[int, int]) -> int:
        pass

