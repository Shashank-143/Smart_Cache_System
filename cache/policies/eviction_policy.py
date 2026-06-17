class EvictionPolicy:
    """Base class for all eviction policies."""

    def record_access(self, node: Any) -> None:
        """
        Records an access to a node.

        Args:
            node (Any): The accessed node.

        Raises:
            NotImplementedError: If not overridden by subclass.
        """
        raise NotImplementedError

    def evict(self) -> Any:
        """
        Selects a node for eviction.

        Returns:
            Any: The node to be evicted.

        Raises:
            NotImplementedError: If not overridden by subclass.
        """
        raise NotImplementedError
