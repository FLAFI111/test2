import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import os
import json


from bestapp.todo import TodoList
def setup_module(module):
    # ensure a clean tasks file
    if os.path.exists('tasks.json'):
        os.remove('tasks.json')


def test_add_and_list():
    todo = TodoList()
    todo.load()
    todo.add('Write tests')
    todo.add('Pass all tests')
    assert len(todo.list_tasks()) == 2
    assert todo.list_tasks()[0].description == 'Write tests'


def test_complete_and_remove():
    todo = TodoList()
    todo.load()
    todo.complete(0)
    assert todo.list_tasks()[0].done is True
    todo.remove(0)
    assert len(todo.list_tasks()) == 1
    assert todo.list_tasks()[0].description == 'Pass all tests'


def teardown_module(module):
    if os.path.exists('tasks.json'):
        os.remove('tasks.json')
