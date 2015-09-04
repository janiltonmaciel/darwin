# -*- coding:utf-8 -*-

# import system
import locale
from datetime import datetime

try:
    locale.setlocale(locale.LC_ALL, "pt_BR.utf8")
except locale.Error:
    locale.setlocale(locale.LC_ALL, "pt_BR")


def time_ago_in_words(datetime_obj):
    try:
        timedelta = datetime.now() - datetime_obj
    except TypeError:
        # TODO: log?
        return ''

    days = timedelta.days
    hours = (timedelta.seconds / 60) / 60
    minutes = timedelta.seconds / 60

    plural = lambda x: 's' if x > 1 else ''

    if days < 0:
        return u"há uma consulta agendada para o dia %s" % datetime_obj.strftime('%d-%m-%Y')

    # if days > 10:
    #     return u'em %s de %s de %s' % (datetime_obj.day, datetime_obj.strftime(u'%B').lower(), datetime_obj.year)
        # return u'em %s de %s de %s' % (datetime_obj.day, datetime_obj.strftime(u'%B').lower(), datetime_obj.year)

    if days:
        return u'há %s dia%s' % (days, plural(days))

    if hours:
        time_ago_in_words = u'há %s hora%s' % (hours, plural(hours))

        if minutes % 60:
            time_ago_in_words = u'%s e %s minuto%s' % (time_ago_in_words, minutes % 60, plural(minutes % 60))
        return time_ago_in_words

    if minutes:
        return u'há %s minuto%s' % (minutes, plural(minutes))

    return u'há menos de um minuto'
