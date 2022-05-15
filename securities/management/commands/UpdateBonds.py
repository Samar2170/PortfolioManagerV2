from django.core.management.base import BaseCommand
from securities.loaders.bonds import load_listed_ncd

class Command(BaseCommand):
    def handle(self, *args, **options):
        load_listed_ncd()