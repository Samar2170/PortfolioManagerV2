from django.core.management.base import BaseCommand
import pandas as pd
from securities.models.stocks import Stock
from securities.loaders.stocks import load_stocks
from securities.loaders.mf import load_mutual_funds

class Command(BaseCommand):
    def handle(self, *args, **options):
        load_stocks()
        load_mutual_funds()
            