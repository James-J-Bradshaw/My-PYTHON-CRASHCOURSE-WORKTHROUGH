import pytest
from employees import Employee

@pytest.fixture
def template_employee():
    """A template for test employee functions"""
    first = "James"
    last = "Bradshaw"
    salary = 25000
    template = Employee(first, last, salary)
    return template

def test_default_increase(template_employee):
    """Test to see if employee's annual salary is increased by £5,000"""
    template_employee.give_default_raise()
    assert template_employee.salary == 30000

def test_custom_increase(template_employee):
    """Test to see if employee's annual salary can be increased by a custom number"""
    custom = 10000
    template_employee.give_custom_raise(custom)
    assert template_employee.salary == 35000