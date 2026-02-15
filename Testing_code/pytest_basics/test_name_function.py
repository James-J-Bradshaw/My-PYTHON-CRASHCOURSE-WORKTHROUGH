from name_function import get_formatted_name
def test_first_last_name():
        """Do names like Janis Joplin work?"""
        formatted_name = get_formatted_name("Janis", "Joplin")
        assert formatted_name == "Janis Joplin"

def test_first_last_middle_name():
        """does names like Wolfgang Armadeus Mozart"""
        formatted_name = get_formatted_name(
                "wolfgang", "armadeus", "mozart"
        )
        assert formatted_name == "Wolfgang Armadeus Mozart"