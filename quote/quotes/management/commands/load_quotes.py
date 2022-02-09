from django.core.management.base import BaseCommand
from scrap import my_scrap
from quotes.models import *
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = 'Loads quotes from https://quotes.toscrape.com/page/<page:int>/ into db.'

    def add_arguments(self, parser):
        parser.add_argument('pages', nargs=1, type=int)

    def handle(self, *args, **options):
        pages = options['pages'][0]

        data = my_scrap(pages)
        self.stdout.write(self.style.SUCCESS(f'len data{len(data)}'))
 
        authors = set()
        tags = set()
        for one_data in data:
            authors.add(one_data['author'])
            [tags.add(t) for t in one_data['tags']]

        

        _ = Author.objects.bulk_create(
            [Author(name=name) for name in authors],
            ignore_conflicts=True,)

        _ = Tag.objects.bulk_create(
            [Tag(name=name) for name in tags],
            ignore_conflicts=True,)

        all_tags = Tag.objects.all()

        quote_list = []
        for one_data in data:
            #autor_id-it is author name
            author_id = one_data['author']
            quote_tags = [Tag.objects.get(name=name) for name in one_data['tags']]
            text = one_data['quote']
            quote_instance = Quote.objects.get_or_create(text=text,author_id=author_id)[0]
            quote_instance.tags.add(*quote_tags)


