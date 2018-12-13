from django.core.mail import send_mail
from django.template.loader import render_to_string

from rentalmoose.settings import TEMPLATES_PATH


class EmailHandler:

    @staticmethod
    def send_email(subject, to, filename, params, from_email="noreply@rentalmoose.ca", ):

        #both txt and html should be named the same, and they should be inside a folder with the same name!
        #eg. /templates/emails/welcome/welcome.txt
        #/templates/emails/welcome/welcome.html

        plain_text_path = TEMPLATES_PATH + "/templates/emails/{}/".format(filename) + filename + ".txt"
        html_path = TEMPLATES_PATH + "/templates/emails/{}/".format(filename) + filename + ".html"

        msg_plain = render_to_string(plain_text_path, params)
        msg_html = render_to_string(html_path, params)

        return send_mail(
            subject,
            msg_plain,
            from_email,
            to,
            html_message=msg_html,
        )