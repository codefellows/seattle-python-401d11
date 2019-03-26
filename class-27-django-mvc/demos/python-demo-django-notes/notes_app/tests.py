from django.test import TestCase, RequestFactory
from .models import Note


class TestNotesModels(TestCase):
    def setUp(self):
        Note.objects.create(title='title one', detail='detail one')
        Note.objects.create(title='title two', detail='detail two')
        Note.objects.create(title='title three', detail='detail three')

    def test_note_titles(self):
        one = Note.objects.get(title='title one')
        two = Note.objects.get(title='title two')
        self.assertEqual(one.title, 'title one')
        self.assertEqual(two.title, 'title two')

    def test_note_detail(self):
        one = Note.objects.get(title='title one')
        two = Note.objects.get(title='title two')
        self.assertEqual(one.detail, 'detail one')
        self.assertEqual(two.detail, 'detail two')


class TestNotesViews(TestCase):
    def setUp(self):
        self.request = RequestFactory()

        Note.objects.create(title='title one', detail='detail one')
        Note.objects.create(title='title two', detail='detail two')
        Note.objects.create(title='title three', detail='detail three')

    def test_note_detail_view_context(self):
        from .views import note_detail_view
        request = self.request.get('')
        response = note_detail_view(request, f'{ Note.objects.get(title="title one").id }')
        self.assertIn(b'detail one', response.content)

    def test_note_list_view_context(self):
        from .views import note_list_view
        request = self.request.get('')
        response = note_list_view(request)
        self.assertIn(b'title two', response.content)

    def test_note_detail_view_status_code_success(self):
        from .views import note_detail_view
        request = self.request.get('')
        response = note_detail_view(request, f'{ Note.objects.get(title="title one").id }')
        self.assertEqual(response.status_code, 200)

    def test_note_list_view_status_code_success(self):
        from .views import note_list_view
        request = self.request.get('')
        response = note_list_view(request)
        self.assertEqual(response.status_code, 200)

    def test_note_detail_view_status_code_failure(self):
        from .views import note_detail_view
        from django.http import Http404
        request = self.request.get('')
        with self.assertRaises(Http404):
            note_detail_view(request, '0')

