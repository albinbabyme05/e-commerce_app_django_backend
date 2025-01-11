from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(list_data, chunk_size):
    """Splits a list into chunks of the given size."""
    chunk = []
    i = 0
    for data in list_data:
        chunk.append(data)
        i += 1
        if i == chunk_size:
            yield chunk
            chunk = []
    if chunk:  # Handle remaining items
        yield chunk
