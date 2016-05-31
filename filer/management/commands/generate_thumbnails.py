# -*- coding: utf-8 -*-
'''
Created on May 31, 2016

@author: jakob
'''

from django.core.management.base import BaseCommand
from filer.models.imagemodels import Image


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        pks = Image.objects.all().values_list('id', flat=True)
        total = len(pks)
        for idx, pk in enumerate(pks):
            image = None
            try:
                image = Image.objects.get(pk=pk)
                self.stdout.write('Processing image %i / %i %s' % (idx + 1, total, str(image).decode('utf-8')))
                self.stdout.flush()
                image.thumbnails
                image.icons
            except IOError, e:
                self.stderr.write('Failed to generate thumbnails: %s' % str(e))
                self.stderr.flush()
            finally:
                del image
