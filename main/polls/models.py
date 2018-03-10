# -*- coding: utf-8 -*-
from django.db import models


class Base(models.Model):
    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.created


class Option(Base):
    text = models.TextField(
        verbose_name='Text'
    )

    image = models.ImageField(
        verbose_name='Imagem',
        upload_to='option/images/', 
        null=True,
        blank=True,
    )

    poll = models.ForeignKey(
        'Poll', 
        on_delete=models.CASCADE,
        related_name='options_poll'
    )

    class Meta:
        verbose_name = "Option"

    def __str__(self):
        return self.text


class Poll(Base):
    title = models.CharField(
        max_length = 150,
        verbose_name='Title'
    )

    text = models.TextField(
        verbose_name='Text'
    )

    class Meta:
        verbose_name = "Poll"

    def __str__(self):
        return self.text


class PollSummary(Poll):
    class Meta:
        proxy = True
        verbose_name = 'Poll Summary'
        verbose_name_plural = 'Polls Summary'


class Vote(Base):
    poll = models.ForeignKey(
        'Poll', 
        on_delete=models.CASCADE,
        related_name='votes_poll'
    )

    options = models.ForeignKey(
        'Option', 
        on_delete=models.CASCADE,
        related_name='votes_option'
    )

    class Meta:
        verbose_name = "Vote"

