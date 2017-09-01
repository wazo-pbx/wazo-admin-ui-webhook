# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask import render_template
from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView

from .form import WebhookFormHTTP


class WebhookView(BaseView):

    form = WebhookFormHTTP
    resource = 'webhook'

    @classy_menu_item('.webhooks', 'Webhooks', order=10, icon="globe")
    def index(self):
        return super(WebhookView, self).index()

    def _populate_form(self, form):
        form.services.choices = self._build_choices_services()
        return form

    def _build_choices_services(self):
        services = self.service.list_services()
        services_list = [((''), ('Choose a service'))]
        for service in services['services']:
            services_list.append((service, service))
        return services_list
