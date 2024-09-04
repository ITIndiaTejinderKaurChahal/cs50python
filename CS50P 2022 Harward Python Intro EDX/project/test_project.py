import pytest
from unittest.mock import patch
from project.project import get_cpu_utilization, get_memory_utilization, get_disk_utilization, generate_report

# Mocking psutil.cpu_percent
@patch('project.psutil.cpu_percent')
def test_get_cpu_utilization(mock_cpu_percent):
    mock_cpu_percent.return_value = 75.0
    assert get_cpu_utilization() == 75.0

# Mocking psutil.virtual_memory
@patch('project.psutil.virtual_memory')
def test_get_memory_utilization(mock_virtual_memory):
    mock_virtual_memory.return_value.percent = 60.0
    assert get_memory_utilization() == 60.0

# Mocking psutil.disk_usage
@patch('project.psutil.disk_usage')
def test_get_disk_utilization(mock_disk_usage):
    mock_disk_usage.return_value.percent = 80.0
    assert get_disk_utilization() == 80.0

# Mocking file write operation for report generation
@patch('project.open', new_callable=pytest.mock.mock_open)
@patch('project.get_cpu_utilization')
@patch('project.get_memory_utilization')
@patch('project.get_disk_utilization')
def test_generate_report(mock_get_disk_utilization, mock_get_memory_utilization, mock_get_cpu_utilization, mock_open):
    mock_get_cpu_utilization.return_value = 55.0
    mock_get_memory_utilization.return_value = 65.0
    mock_get_disk_utilization.return_value = 70.0

    generate_report()

    # Check if the file was written with the expected content
    mock_open.assert_called_once_with('resource_report.txt', 'w')
    handle = mock_open()
    handle.write.assert_called_once_with(
        "Server Resource Utilization Report\n"
        "---------------------------------\n"
        "CPU Utilization: 55.0%\n"
        "Memory Utilization: 65.0%\n"
        "Disk Utilization: 70.0%\n"
    )
