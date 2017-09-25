# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

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
        form.user_uuid.choices = self._build_setted_choices_users(form.events_user_uuid)
        return form

    def _map_resources_to_form(self, resource):
        resource['events'] = resource.get('events')[0]
        resource['services'] = resource.get('service')

        resource['url'] = resource['config'].get('url')
        resource['body'] = resource['config'].get('body')
        resource['verify_certificate'] = resource['config'].get('verify_certificate')
        resource['method'] = resource['config'].get('method')
        resource['content_type'] = resource['config'].get('content_type')

        form = self.form(data=resource)
        return form

    def _build_choices_services(self):
        services = self.service.list_services()
        services_list = [((''), ('Choose a service'))]
        for service in services['services']:
            services_list.append((service, service))
        return services_list

    def _build_setted_choices_users(self, user_uuid):
        if not user_uuid.data or user_uuid.data == 'None':
            return []
        return [(user_uuid.data, user_uuid.data)]
