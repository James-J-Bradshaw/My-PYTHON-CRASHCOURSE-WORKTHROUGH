def get_formatted_name(first, last, middle=""):
    if middle:
        swap = last
        last = middle
        middle = swap
        formatted_name = f"{first} {middle} {last}"
    else:
        formatted_name = f"{first} {last}"
    
    return formatted_name.title()