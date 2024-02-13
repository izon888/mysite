import os

from lorem import *
from random import randint, choice
from .models import News, Category


def create_news():
    for i in range(1, 50):
        title = get_sentence(count=randint(1, 5), comma=(0, 2), word_range=(4, 8), sep=' ')
        content = get_paragraph(count=randint(1, 8), comma=(0, 2), word_range=(4, 8), sentence_range=(5, 10),
                                sep=os.linesep)
        category = choice(Category.objects.all())
        News.objects.create(title=title, content=content, category=category)
        print(f'News {i} was added')

