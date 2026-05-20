"""Helper utility functions."""


def format_response(data: dict) -> str:
    """Format response data.
    
    Args:
        data: Data dictionary
        
    Returns:
        Formatted string
    """
    return str(data)


def parse_input(text: str) -> dict:
    """Parse input text.
    
    Args:
        text: Input text
        
    Returns:
        Parsed dictionary
    """
    return {"input": text}
