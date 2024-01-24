from django.test import TestCase
from django.urls import reverse
from .models import ToDoList, ToDoItem


class ToDoListViewTests(TestCase):
    def test_list_list_view_uses_correct_template(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "todo/index.html")

    def test_list_list_view_displays_lists(self):
        # Create a ToDoList instance for testing
        ToDoList.objects.create(title="Test List")

        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test List")


class ToDoItemViewTests(TestCase):
    def setUp(self):
        # Create a ToDoList instance for testing
        self.todo_list = ToDoList.objects.create(title="Test List")

        # Create a ToDoItem instance for testing
        self.todo_item = ToDoItem.objects.create(
            todo_list=self.todo_list, title="Test Item"
        )

    def test_item_list_view_uses_correct_template(self):
        response = self.client.get(reverse("list", args=[self.todo_list.id]))
        self.assertTemplateUsed(response, "todo/todo_list.html")

    def test_item_list_view_displays_items(self):
        response = self.client.get(reverse("list", args=[self.todo_list.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Item")

    def test_item_delete_view_success(self):
        response = self.client.post(
            reverse("item-delete", args=[self.todo_list.id, self.todo_item.id])
        )
        self.assertRedirects(response, reverse("list", args=[self.todo_list.id]))
