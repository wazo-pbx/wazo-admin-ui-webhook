# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask import g
from flask_login import current_user
from werkzeug.local import LocalProxy

from wazo_webhookd_client import Client as WebhookdClient
from wazo_admin_ui.helpers.confd import confd

class WebhookService(object):

    def __init__(self):
        self.webhookd = webhookd

    def list(self):
        return self.webhookd.subscriptions.list()

    def create(self, resource):
        subscription = {
          'name': resource.get('name'),
          'service': resource.get('services'),
          'events': [resource.get('events')],
          'config': {
            'url': resource.get('url'),
            'content_type': resource.get('content_type'),
            'method': resource.get('method'),
            'body': resource.get('body', ""),
            'verify_certificate': resource.get('verify_certificate', 'false')
          }
        }

        return self.webhookd.subscriptions.create(subscription)

    def get(self, uuid):
        return self.webhookd.subscriptions.get(uuid)

    def delete(self, uuid):
        return self.webhookd.subscriptions.delete(uuid)

    def update(self, resource):
        webhook_id = resource.get('id')
        return self.webhookd.subscriptions.update(webhook_id, resource)

    def list_services(self):
        return self.webhookd.subscriptions.list_services()


def get_webhookd_client():
    client = g.get('get_webhookd_client')
    if not client:
        client = g.get_webhookd_client = WebhookdClient('localhost', verify_certificate=False)
        token = current_user.get_id()
        client.set_token(token)

    return client

webhookd = LocalProxy(get_webhookd_client)
