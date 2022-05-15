from django.core.management.base import BaseCommand
from securities.loaders.stocks import load_stocks
from securities.loaders.mf import load_mutual_funds

class Command(BaseCommand):
    def handle(self, *args, **options):
        load_stocks()
        load_mutual_funds()
            