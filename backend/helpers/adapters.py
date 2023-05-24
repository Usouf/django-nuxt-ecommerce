import logging

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

log = logging.getLogger(__name__)

class EmailAdapter(object):
    def render_mail(self, template_prefix, emails, context):
        """
        Renders an e-mail to `email`.  `template_prefix` identifies the
        e-mail that is to be sent, e.g. "account/email/email_verification"
        """
        log.info("render_mail")
        subject = render_to_string('{0}_subject.txt'.format(template_prefix), context)

        # remove superfluous line breaks
        subject = " ".join(subject.splitlines()).strip()

        template_name = '{0}_message.html'.format(template_prefix)
        message = render_to_string(template_name, context).strip()

        msg = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, emails)
        msg.content_subtype = 'html'  # Main content is now text/html
        return msg

    # emails should be a list of emails
    def send_mail(self, template_prefix, emails, context, cc=None):
        msg = self.render_mail(template_prefix, emails, context)
        log.info("context: %s", context)

        if cc:
            log.info("has cc: %s" % cc)
            msg.cc = cc

        msg.send()